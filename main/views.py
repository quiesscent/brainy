from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Subject, Lesson, UserProfile, CustomUser, Test, Score, Answer
# Create your views here.

def index(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'index.html', context)


def login_(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome back')
            return redirect('/classes')
        else:
            messages.error(request, 'Wrong login details, try again')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        user = CustomUser.objects.filter(email=email)
        if user:
            messages.error(request, 'User already registered')
            return redirect('/login')
        if password2 != password1:
            messages.error(request, 'Passwords don\'t match')
            return redirect('/register')

        my_user = CustomUser.objects.create_user(username, email, password1)
        my_user.save()
        messages.success(request, 'User Created Successfully. Login')
        return redirect('/login')

    return render(request, 'signup.html')


def about(request):
    return render(request, 'about.html')


def classes(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'classes.html', context)


def classes_details(request, pk):
    subject = Subject.objects.get(id=pk)
    lessons = Lesson.objects.filter(subject=pk)
    context = {
        'subject': subject,
        'lessons': lessons
    }
    return render(request, 'course_details.html', context)

def learn(request, pk):
    subject = Subject.objects.get(id=pk)
    lessons = Lesson.objects.filter(subject=pk)
    context = {
        'subject': subject,
        'lessons': lessons
    }
    return render(request, 'learn.html', context)


def test(request, pk ):
    lesson = Lesson.objects.get(id=pk)
    test = Test.objects.filter(lesson=pk)
    context = {
        'lesson': lesson,
        'test': test
    }
    if request.method == 'POST':
        answer = request.POST['answer']


        answer = Answer(user=request.user.username, answer=answer, lesson=lesson)

        answer.save()
        messages.success(request, 'Test Completed Please wait for your scores....')
        return redirect(f'/learn/{pk}')

    return render(request, 'test.html', context)


def contact(request):
    return render(request, 'contact.html')


def leaderboard(request):
    leader = Score.objects.all()
    context = {
        'score': leader,
    }
    return render(request, 'leaderboard.html', context)

def logout_(request):
    logout(request)
    messages.info(request, "Logged Out")
    return redirect('/')
from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce import models as tinymce_models
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email


class Subject(models.Model):
    title = models.CharField(default='', max_length=100)
    grade = models.CharField(default='1 - 8 ', max_length=10)
    duration = models.CharField(default='4 Weeks', max_length=20)
    details = models.TextField(default='')
    image = models.ImageField(upload_to='static/img/subjects/', default='default')
    objectives = tinymce_models.HTMLField(max_length=100000, default='')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Subjects'


class Lesson(models.Model):
    '''Model definition for Lesson.'''
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    description = models.TextField(default='')

    class Meta:
        '''Meta definition for Lesson.'''
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title


class Score(models.Model):
    '''Model definition for Score.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField(default='')

    class Meta:
        '''Meta definition for Score.'''

        verbose_name = 'Score'
        verbose_name_plural = 'Scores'

    def __str__(self):
        return self.user + self.subject + "Scores"


class UserProfile(models.Model):
    '''Model definition for UserProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='static/img/profiles/', default='default')

    class Meta:
        '''Meta definition for UserProfile.'''

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.user + 'Profile'

class Test(models.Model):
    '''Model definition for Test.'''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    questions =  tinymce_models.HTMLField(max_length=100000, default='')
    score = models.IntegerField(default=0)

    class Meta:
        '''Meta definition for Test.'''

        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return f"{self.lesson} Test"

class Answer(models.Model):
    '''Model definition for Answer.'''
    user = models.CharField(default='', max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=1)
    answer = models.TextField(default='')
    class Meta:
        '''Meta definition for Answer.'''

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.test + "Answer"

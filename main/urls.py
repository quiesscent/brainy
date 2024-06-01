from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('classes', views.classes, name='classes'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_, name='login'),
    path('logout', views.logout_, name='logout'),
    path('register', views.register, name='register'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('learn/<int:pk>', views.learn, name="learn"),
    path('learn/test/<int:pk>', views.test, name="test"),
    path('classes/details/<int:pk>', views.classes_details, name='c_details'),
]

from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('profile',profile,name='profile'),
    path('home',home,name='home'),
    path('friends',friends,name='friends'),
    path('message',message,name='message'),
   
]


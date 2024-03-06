from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'profile.html')
def home(request):
    return render(request,'home.html')
def friends(request):
    return render(request,'friends.html')
def message(request):
    return render(request,'message.html')
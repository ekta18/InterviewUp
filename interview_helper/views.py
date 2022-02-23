from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

# @unauthorized_user
def registerpage(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

def faqspage(request):
    return render(request,'faqs.html')

def overviewpage(request):
    return render(request,'overview.html')


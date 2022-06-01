from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from .functions import handle_uploaded_file
# from .forms import ResumeForm 

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def faqspage(request):
    return render(request,'faqs.html')

def overviewpage(request):
    return render(request,'overview.html')

def resumeinput(request):
    return render(request,'resumeinput.html')

def registerpage(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('email')
            # email=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')
            # user_list=User.objects.all()
            # for query in user_list:
            #     if user.username in query.username:
            #         error = "Email Already Exists . "
            #         return render(request, 'signup.html', {'form': form,'error':error})
            return redirect('login')
    context={'form':form}
    return render(request,'signup.html',context)

def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = email.split("@")[0]
        print(name)
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print(email)
        print(password)
        print(user)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = "Invalid Email id or Password. Please Try Again!!"
            return render(request,"login.html",{'message':message})
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

# def resumeinput(request):  
#     if request.method == 'POST':  
#         resume = ResumeForm(request.POST, request.FILES)  
#         if resume.is_valid():  
#             handle_uploaded_file(request.FILES['file'])  
#             model_instance = resume.save(commit=False)
#             model_instance.save()
#             return HttpResponse("File uploaded successfuly")  
#     else:  
#         resume = ResumeForm()  
#         return render(request,"resumeinput.html",{'form':resume})  

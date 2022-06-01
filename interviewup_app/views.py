from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .functions import handle_uploaded_file
import fitz
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

def experiencevideospage(request):
    return render(request,'experiencevideos.html')

def domainpage(request):
    return render(request,'domain.html')

def newspage(request):
	technews = Tech_News.objects.all()
	startupnews = Tech_Startup.objects.all()
	return render(request,'news.html',{'technews':technews,'startupnews':startupnews})

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

def showfile(request):
    lastfile= File.objects.last()
    filepath= lastfile.filepath
    print(filepath)
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        with fitz.open(filepath.path) as doc:
        	data = ""
        	for page in doc:
        		data += page.get_text()
        print(data)
        keyword1 = 'ACHIEVEMENTS:'
        keyword2 = 'EDUCATION:'
        keyword3 = 'PROJECTS:'
        keyword4 = 'SKILLS:'
        keyword5 = 'EXPERIENCE:'
        text = data
        experience = text.partition(keyword5)[2]
        text = text.partition(keyword5)[0]

        skills = text.partition(keyword4)[2]
        text = text.partition(keyword4)[0]

        project = text.partition(keyword3)[2]
        text = text.partition(keyword3)[0]

        education = text.partition(keyword2)[2]
        text = text.partition(keyword2)[0]

        achievements = text.partition(keyword1)[2]
        text = text.partition(keyword1)[0]

        print(achievements)
        print(education)
        print(project)
        print(skills)
        print(experience)

        #domain detection
        if('Auditing' in skills):
        	domain_id = 1
        	print(domain_id)
        	request.session['domain_id'] = domain_id

        elif('Artistic skills' in skills):
        	domain_id = 2
        	print(domain_id)
        	request.session['domain_id'] = domain_id

        elif('Machine Learning' in skills):
        	domain_id = 3
        	print(domain_id)
        	request.session['domain_id'] = domain_id

        elif('Mechanical Design' in skills):
        	domain_id = 4
        	print(domain_id)
        	request.session['domain_id'] = domain_id

        elif('MATLAB' in skills):
        	domain_id = 5
        	print(domain_id)
        	request.session['domain_id'] = domain_id

        return redirect('domain')

    context= {'filepath': filepath,'form': form}
    return render(request, 'resumeinput.html', context)


def domainpage(request):
	domain_id = request.session.get('domain_id')
	print(domain_id)
	dname = Domain.objects.filter(did=domain_id)
	question = Question.objects.filter(did=domain_id)
	roles_companies = RolesCompanies.objects.filter(did=domain_id)

	context= {'dname':dname, 'question': question, 'roles_companies': roles_companies}
	return render(request, 'domain.html', context)


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

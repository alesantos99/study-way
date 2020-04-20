from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.http import HttpResponse
from .models import User,  Study, Theme

def signup(request):
    if request.method == 'POST':

        form = SingUpForm(request.POST)

        if form.is_valid():
            
            form.save()
            user = form.save(commit=False)
            user.refresh_from_db();
            
            user.set_password(form.cleaned_data['password1'])
            user.save()
            username = form.cleaned_data['username']
            
            password = form.cleaned_data['password1']
            
            user = authenticate(request,username=username, password=password)
            
            login(request, user)
            
            return redirect('register-teacher')
        else:
            return render(request,'register.html',{'form': form})
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/teacher-page')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def create_study(request):
    
    data = {}

def list_user(request,id):

    user = get_object_or_404(User,pk=id)
  
    return render(request, 'userpage.html',{'user':user})

#@login_required
"""def register_teacher(request):
    data = {}   
     
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        
        form.save()

        return redirect('register-teacher')
    data['form'] = form
    return render(request, 'register-teacher.html', data)   



def list_study(request, id):
    
    studies = Stduy.objects.filter(user = id)

    return render(request, 'studiespage.html',{'studies':studies})



def list_teacher(request):

    professor = Professor.objects.all()
    return render(request, 'teacher-page.html',{'professor':professor})

def update_teacher(request,id):
    data ={}
    professor = get_object_or_404(Professor,pk=id)
    form = ProfessorForm(request.POST or None, instance= professor)
    if form.is_valid():
        form.save()
        return redirect('teacher-page')
    data['form'] = form
    return render(request, 'register-teacher.html', data)  

def register_student(request):
    data={}
    
    form = StudentForm(request.POST or None )

    if form.is_valid():
        form.save()
        return redirect('register-student')
    data['form']= form
    return render(request, 'register-student.html' , data)
        """
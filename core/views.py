from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .forms import ProfessorForm , StudentForm
from .models import Professor
#@login_required
def register_teacher(request):
    data = {}    
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('register-teacher')
    data['form'] = form
    return render(request, 'register-teacher.html', data)   

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
        
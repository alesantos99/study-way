from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.http import HttpResponse
from .models import User,  Study, Theme, Test, TestUser, Question, UserQuestion, Option
from core.forms import SingUpForm
from django.contrib.auth.views import LoginView

def home(request):
    
    return render(request, 'index.html')

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
            
            return redirect('signin')
        else:
            return render(request,'register.html',{'form': form})
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles/user')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def usepage(request):
    #url = '/userpage/%s/' % request.user.username
    username = request.user.username
    print(username)
    return redirect('userpage', username)
def showtests(request,id):

    tests = Test.objects.all()

    user = User.objects.get(username = id)
    return render(request, 'tests.html', {'tests':tests, 'user':user})

def showtestdetail(request,id,username):

    test = Test.objects.get(name = id)
    
    user = User.objects.get(username = username)
    #name = user.username
    testuser = TestUser.objects.filter(user = username, test = test.id)
    teststarted = True
    
    if testuser.count() == 0:
        teststarted = False
    return render(request, 'testpage.html', {'test':test, 'user':user,'testuser':testuser,'teststarted':teststarted})

def startest(request,id, username):

    test = Test.objects.get(name = id)

    
    user = User.objects.get(username = username)

  
    
    content = list()

    for q in test.questions.all():

        questions = Question.objects.filter(name = q.name)   

    
    for qt in questions:
        
        options = Option.objects.filter(question = qt.id) 
        content.append((qt, options))

    cont = dict(content)

    answ = list()

    question_scores = test.total_score/test.number_question  
            
   
    user_scores = 0

    correct_answers = 0

    print('Scores',user_scores) 

    if(request.POST):
       

        for qt in test.questions.all():
            q = request.POST[str(qt.id)]
            answ.append((qt.name,(q,qt.question_answer)))
        answers = dict(answ)
        
        for key in answers:
            #print(answers[key][0])
            user_question = UserQuestion()
            
            user_question.user = user
            
            user_question.question = Question.objects.get(name = key)
            
            user_question.answer = [key][0]

            if answers[key][0] == answers[key][1]:

                user_scores = user_scores +question_scores
                
                correct_answers +=1

                user_question.correct_answer = True
            
            else:
                
                user_question.correct_answer = False
            
            user_question.is_done = True

            user_question.save()
        testuser = TestUser()
        
        testuser.user = user
        
        testuser.test = test
        
        testuser.user_score = user_scores
        
        testuser.correct_answers =  correct_answers
        
        testuser.started = True
        
        testuser.completed = True

        testuser.save()    
      
        return redirect('finishedtest',id,username) 
       
    data={}
  
    

    return render(request, 'testuser.html', {'test': test, 'user':user,'content:': cont})

def finishedtest(request,id, username):
    
    user = User.objects.get(username = username)
    
    test = Test.objects.get(name = id)
    
    testuser = TestUser.objects.get(user = user.username, test = test.id )
    
    accurance = str((testuser.user_score / test.total_score)*100) 
    
    return render(request, 'finishedtest.html', {'user':user, 'test':test, 'testuser':testuser,'accurance':accurance}) 


def repeatest(request,id, username):
    
    test = Test.objects.get(name = id)

    
    user = User.objects.get(username = username)

  
    
    content = list()

    for q in test.questions.all():

        questions = Question.objects.filter(name = q.name)   

    
    for qt in questions:
        
        options = Option.objects.filter(question = qt.id) 
        content.append((qt, options))

    cont = dict(content)

    answ = list()

    question_scores = test.total_score/test.number_question  
            
   
    user_scores = 0

    correct_answers = 0

    print('Scores',user_scores) 
    
    if(request.POST):
       

        for qt in test.questions.all():
            q = request.POST[str(qt.id)]
            answ.append((qt.name,(q,qt.question_answer)))
        answers = dict(answ)
        
        for key in answers:
            #print(answers[key][0])
            question = Question.objects.get(name = key)
            #user_question = UserQuestion.objects.get(user = user.username, question = question.id)
            
            #user_question.user = user
            
            #user_question.question = Question.objects.get(name = key)
            ans = [key][0]
            #user_question.answer = [key][0]

            if answers[key][0] == answers[key][1]:

                user_scores = user_scores +question_scores
                
                correct_answers +=1
                correct = True
                #user_question.correct_answer = True
            
            else:
                correct = False
                #user_question.correct_answer = False
            isdone = True
            #user_question.is_done = True
            UserQuestion.objects.filter(user = user.username, question = question.id).update(answer = ans, correct_answer = correct, is_done = isdone)

            #user_question.save()
        testuser = TestUser.objects.get(user = user.username,test= test.id)
        
        testuser.user = user
        
        testuser.test = test
        
        testuser.user_score = user_scores
        
        testuser.correct_answers =  correct_answers
        
        testuser.started = True
        
        testuser.completed = True

        testuser.save()    
      
        return redirect('finishedtest',id,username) 
       
    data={}
  
    

    return render(request, 'testuser.html', {'test': test, 'user':user,'content:': cont})

    #>>> Entry.objects.filter(blog__id=1).update(comments_on=True)


def create_study(request):
    
    data = {}

def list_user(request,id):

    user = get_object_or_404(User,pk=id)
  
    return render(request, 'userpage.html',{'user':user})

def redirectests(request, id):

    return redirect('tests', id)
 
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
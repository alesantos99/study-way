from django.forms import ModelForm, Form
from django import forms
from .models import User, Test, Question, Option, TestUser, UserQuestion
from django.contrib.auth.forms import UserCreationForm

USER_CHOICES =( 
    ("TC", "Teacher"), 
    ("ST", "Student")
) 

class SingUpForm(UserCreationForm):

    first_name = forms.CharField( label = 'Nome', max_length=100, required=True, help_text = 'Obrigatório')

    last_name = forms.CharField( label = 'Sobrenome', max_length=100, required=True,help_text = 'Obrigatório')

    email = forms.EmailField(label = 'E-mail',max_length = 254, required=True, help_text = 'Obrigatório')

    
    phone = forms.CharField( label = 'Telefone', max_length=100, required=True,help_text = 'Obrigatório')
    

    
    class Meta:
        
        model = User
            
        fields = ['username']


class TestForm(forms.Form):
    
    quest  = Question.objects
    OP  = (('a','A'))
    def __init__(self, question,*args, **kwargs):
        
        quest = question
        options = list()
        for o in quest.options:

            options.append((str(o.label), str(o.description)))    
        
        return super(TestForm, self).__init__(*args,question, **kwargs)
    
  

   
   
    user = forms.CharField( label = 'Usuário', max_length=100, required=True, help_text = 'Obrigatório')

    question = forms.CharField( label = 'Questão', max_length=100, required=True, help_text = 'Obrigatório') 

    #answer = forms.MultipleChoiceField(choices=options)
   
    class Meta:

        model = UserQuestion
            
        fields = ['user','question']

    

    
        
        
    
    
   
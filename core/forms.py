from django.forms import ModelForm
from django import forms
from .models import Professor, Student, User
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
    

    type_user = forms.ChoiceField(label = 'Tipo do usuário', choices= USER_CHOICES)

    class Meta:
        model = User
            
        fields = ['username','first_name', 'last_name', 'email', 'phone', 'type_user','password1','password2']
    
class ProfessorForm(ModelForm):

    class Meta:

        model = Professor

        fields = ['first_name','last_name', 'email','telefone','user_id','password','photo']


class StudentForm(ModelForm):

    class Meta:

        model = Student

        fields = ['first_name','last_name', 'email','telefone','user_id','password','photo']
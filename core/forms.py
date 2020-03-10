from django.forms import ModelForm
from .models import Professor
from .models import Student


class ProfessorForm(ModelForm):

    class Meta:

        model = Professor

        fields = ['first_name','last_name', 'email','telefone','user_id','password','photo']


class StudentForm(ModelForm):

    class Meta:

        model = Student

        fields = ['first_name','last_name', 'email','telefone','user_id','password','photo']
from django.forms import ModelForm
from .models import Professor


class ProfessorForm(ModelForm):

    class Meta:

        model = Professor

        fields = ['first_name','last_name', 'email','telefone','user_id','password','photo']
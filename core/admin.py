from django.contrib import admin

from .models import Professor
# Register your models here.


class ProfessorAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name','email','telefone','photo']

    list_filter = ['user_id','first_name']

    search_fields= ['user_id','first_name', 'last_name', 'password','photo']

admin.site.register(Professor,ProfessorAdmin)

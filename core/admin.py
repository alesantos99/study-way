from django.contrib import admin

from .models import Professor ,Student
# Register your models here.



class ProfessorAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name','email','telefone','photo']

    list_filter = ['user_id','first_name']

    search_fields= ['user_id','first_name', 'last_name','photo']

class StudentAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name','email','telefone','photo']

    list_filter = ['user_id','first_name']

    search_fields= ['user_id','first_name', 'last_name','photo']

admin.site.register(Professor,ProfessorAdmin)

admin.site.register(Student,StudentAdmin)

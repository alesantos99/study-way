from django.contrib import admin

from .models import Professor ,Student,User, Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display =['user']


class UserAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name','email','phone','photo','type_user']

    list_filter = ['username','first_name','type_user']

    search_fields= ['username','first_name', 'last_name','photo', 'type_user']



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


admin.site.register(User,UserAdmin)


admin.site.register(Profile,ProfileAdmin)

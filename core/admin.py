from django.contrib import admin

from .models import User, Profile, Study, Theme, Test, TestUser, Question,Option, UserQuestion, File
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display =['user']



class StudyAdmin(admin.ModelAdmin):
    
    def get_user(self, object):

        fullname = object.user.first_name+" " + object.user.last_name 
        
        return fullname
    
    

    list_display =['name', 'description', 'get_user']

    list_filter = ['name']

    search_fields = ['name']
    


class UserAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name','email','phone','photo','type_user']

    list_filter = ['username','first_name','type_user']

    search_fields= ['username','first_name', 'last_name','photo', 'type_user']



class ThemeAdmin(admin.ModelAdmin):

    list_display =['name', 'description', 'weight']

    list_filter = ['name']

    search_fields= ['name']

class TestAdmin(admin.ModelAdmin):

    list_display =['name', 'description', 'total_score']

    list_filter = ['name']

    search_fields= ['name']  

class QuestionAdmin(admin.ModelAdmin):

    list_display =['name', 'question_statement']

    list_filter = ['name']

    search_fields= ['name']  

class UserQuestionAdmin(admin.ModelAdmin):

    list_display =['user', 'question','answer', 'correct_answer']

    list_filter = ['question']

    search_fields= ['question']  


class OptionAdmin(admin.ModelAdmin):
    model = Option

    list_display =['label','description', 'is_correct']

class FileAdmin(admin.ModelAdmin):
    
    list_display =['filename','extension']

    list_filter = ['filename']

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Theme,ThemeAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(UserQuestion,UserQuestionAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(File,FileAdmin)





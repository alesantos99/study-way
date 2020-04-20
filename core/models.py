import base64

from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractBaseUser):
   
    username = models.CharField(max_length = 100, null = False,blank = False, primary_key = True,  default='----')

    USERNAME_FIELD = 'username'
    objects =  UserManager()
    

    password = models.CharField(max_length = 100, null= False, blank= False, default='---')

    first_name = models.CharField(max_length = 100, null= False, blank= False,default='---')

    last_name = models.CharField(max_length = 100, null= False, blank= False, default='---')



    email = models.EmailField( max_length= 100, null = False, blank = False, default='---')
    
    phone = models.CharField(max_length = 100, null= False, blank= False, default='---')

    photo =  models.ImageField(null= True, blank=True,upload_to='users')
    
    class TypeUser(models.TextChoices):

        TEACHER = 'TC',('Teacher')
        STUDENT = 'ST',('Student')
    

    type_user = models.CharField(max_length= 2, choices = TypeUser.choices, default = TypeUser.STUDENT)

    class Meta:

        verbose_name_plural = 'Users'

    def getTypeUser(self):
        return self.type_user    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects =  UserManager()    

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            u = Profile.objects.create(user=instance)
        instance.profile.save()
        Profile.objects.create_user(User.username, User.password, User.email.lowercase())


class Theme(models.Model):
    
    def get_theme(self):
        return self.name

    name = models.CharField(max_length=200,null= False, blank = False, default= "------")

    description = models.CharField(max_length=500,null= True, blank = True)

    weight = models.IntegerField(null=False,blank= False, default= 0)




class Study(models.Model):

    user = models.ForeignKey("User", on_delete = models.CASCADE, related_name = "studies")

    name = models.CharField(null = False, blank= False, max_length= 100)

    description = models.CharField(null= True, blank = True, max_length = 500)

    themes = models.ManyToManyField(Theme, null = True)



class Question(models.Model):

    name = models.CharField(max_length = 100, null= False, blank= False)    

    question_statement = models.CharField(max_length = 1000, null= False, blank= False)    

    
class Option(models.Model):
    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    label = models.CharField(max_length = 50, null= False, blank= False)    
    
    description = models.CharField(max_length = 500, null= False, blank= False)    

    is_correct = models.BooleanField(null = False, blank= False, default = False)

class Test(models.Model):

    name = models.CharField(null = False, blank= False, max_length= 100)

    description = models.CharField(null= True, blank = True, max_length = 500)

    total_score = models.IntegerField(null=False,blank= False)
    
    number_question = models.IntegerField(null=False,blank= False)

    users = models.ManyToManyField(User)

    questions = models.ManyToManyField(Question)

class TestUser(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    
    user_score = models.IntegerField(null=False,blank= False)

    correct_answers = models.IntegerField(null=False,blank= False)

    timestamp = models.DateTimeField(auto_now_add=True)
    
    completed = models.BooleanField(default=False)


class UserQuestion(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    answer = models.CharField(max_length = 50,null=False,blank= False)

    correct_answer = models.CharField(max_length = 50, null=False,blank= False)

    timestamp = models.DateTimeField(auto_now_add=True)
    
    is_done = models.BooleanField(default=False)

class File(models.Model):
    
    filename = models.CharField(max_length = 100,null=False,blank= False)
    extension = models.CharField(max_length = 50,null=False,blank= False)

    _data = models.TextField(
            db_column='data',
            blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
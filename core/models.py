import base64

from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, UserManager, BaseUserManager,User, PermissionsMixin 
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self,username, password = None):
        
        if not username:
            raise ValueError("O usuário precisa de um username")
        user = self.model(username= username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,username, password = None):

        user = self.create_user(username= username, password = password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
class User(AbstractBaseUser):
   
    username = models.CharField(max_length = 100, null = False,blank = False, primary_key = True,  default='----')

    

    password = models.CharField(max_length = 100, null= False, blank= False, default='---')

    first_name = models.CharField(max_length = 100, null= False, blank= False,default='---')

    last_name = models.CharField(max_length = 100, null= False, blank= False, default='---')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)


    email = models.EmailField( max_length= 100, null = False, blank = False, default='---')
    
    phone = models.CharField(max_length = 100, null= False, blank= False, default='---')

    photo =  models.ImageField(null= True, blank=True,upload_to='users')
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    
    objects =  UserManager()
    
    class Meta:

        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username
    def has_perm(self,perm, obj = None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects =  UserManager()    

   

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

    themes = models.ManyToManyField(Theme)



class Question(models.Model):

    name = models.CharField(max_length = 100, null= False, blank= False)    

    question_statement = models.CharField(max_length = 1000, null= False, blank= False)    

    def getoptions(self):
        
        return Option.objects.filter(question = self)
    def getanswer(self):
        answer = Option.objects.get(question = self, is_correct = True)
        return answer.label 
    def getanswerdescription(self):
        answer = Option.objects.get(question = self, is_correct = True)
        return answer.description
    
    options = property(getoptions)
    
    question_answer = property(getanswer)
    question_answer_description = property(getanswerdescription)
    
class Option(models.Model):
    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    label = models.CharField(max_length = 50, null= False, blank= False)    
    
    description = models.CharField(max_length = 500, null= False, blank= False)    

    is_correct = models.BooleanField(null = False, blank= False, default = False)

class Test(models.Model):

    name = models.CharField(null = False, blank= False, max_length= 100)

    description = models.CharField(null= True, blank = True, max_length = 500)

    total_score = models.IntegerField(null=False,blank= False)
    
    #number_question = models.IntegerField(null=False,blank= False)

    #users = models.ManyToManyField(User)

    questions = models.ManyToManyField(Question)
   
    
    def numberquestions(self):
        
        return self.questions.count() 
    number_question = property(numberquestions)

class TestUser(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    
    user_score = models.IntegerField(null=False,blank= False)

    correct_answers = models.IntegerField(null=False,blank= False)

    timestamp = models.DateTimeField(auto_now_add=True)
    
    completed = models.BooleanField(default=False)
    
    started = models.BooleanField(default=False)

class UserQuestion(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    answer = models.CharField(max_length = 50,null=False,blank= False)

    correct_answer = models.BooleanField(default=False)

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
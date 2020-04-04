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
class Professor(models.Model):
    
    user_id = models.CharField(max_length = 100, null = False,blank = False, primary_key = True)

    password = models.CharField(max_length = 100, null= False, blank= False)

    first_name = models.CharField(max_length = 100, null= False, blank= False)

    last_name = models.CharField(max_length = 100, null= False, blank= False)



    email = models.EmailField( max_length= 100, null = False, blank = False)
    
    telefone = models.CharField(max_length = 100, null= False, blank= False)


    
    photo =  models.ImageField(null= True, blank=True,upload_to='professors')
    #area = models.ForeignKey(Area,  on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = 'Professors'
    def __str__(self):

        return self.user_id

    def getFullName(self):

        return self.first_name + ' '+  self.last_name

class Student(models.Model):
    user_id = models.CharField(max_length = 100, null = False,blank = False, primary_key = True)

    password = models.CharField(max_length = 100, null= False, blank= False)

    
    first_name = models.CharField(max_length=100, null = False, blank=False)
    
    last_name = models.CharField(max_length=100, null = False, blank=False)
    
    email = models.EmailField( max_length= 100, null = False, blank = False) 
    
    telefone = models.CharField(max_length = 100, null= False, blank= False)
    
    photo =  models.ImageField(null= True, blank=True,upload_to='students')
    #area = models.ForeignKey(Area,  on_delete = models.CASCADE)

   
    class Meta:

        verbose_name_plural = 'Students'
    def __str__(self):

        return self.user_id

    def getFullName(self):

        return self.first_name + ' '+  self.last_name

    
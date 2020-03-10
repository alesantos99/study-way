from django.db import models

# Create your models here.

class Professor(models.Model):

    user_id = models.CharField(max_length = 100, null = False,blank = False, primary_key = True)

    
    first_name = models.CharField(max_length = 100, null= False, blank= False)

    last_name = models.CharField(max_length = 100, null= False, blank= False)



    email = models.EmailField( max_length= 100, null = False, blank = False)
    
    telefone = models.CharField(max_length = 100, null= False, blank= False)


    password = models.CharField(max_length = 100, null= False, blank= False)

    photo =  models.ImageField(null= True, blank=True,upload_to='professors')
    #area = models.ForeignKey(Area,  on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = 'Professors'
    def __str__(self):

        return self.user_id

    def getFullName(self):

        return self.first_name + ' '+  self.last_name

class Student(models.Model):

    user_id = models.CharField( max_length=100, null = False, blank=False , primary_key=True)
    
    first_name = models.CharField(max_length=100, null = False, blank=False)
    
    last_name = models.CharField(max_length=100, null = False, blank=False)
    
    email = models.EmailField( max_length= 100, null = False, blank = False) 
    
    telefone = models.CharField(max_length = 100, null= False, blank= False)
    
    password = models.CharField(max_length = 100, null= False, blank= False)
    
    photo =  models.ImageField(null= True, blank=True,upload_to='students')
    #area = models.ForeignKey(Area,  on_delete = models.CASCADE)

   
    class Meta:

        verbose_name_plural = 'Students'
    def __str__(self):

        return self.user_id

    def getFullName(self):

        return self.first_name + ' '+  self.last_name

    
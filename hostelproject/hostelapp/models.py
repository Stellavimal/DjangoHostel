from django.db import models
import datetime
ROOMTYPE_CHOICE=[
   ('Single bed','Single bed'),
   ('Double bed','Double bed'),
   ('More beds','More beds'),
 ]
CATEGORY_CHOICE=[
   ('Admin','Admin'),
   ('Staff','Staff'),
   ('Student','Student'),
    
]
# Create your models here.
class rooms(models.Model):
    Room_id=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    checkin=models.DateField()
    checkout=models.DateField()
    Roomtype=models.CharField(max_length=30,choices=ROOMTYPE_CHOICE)


    class Meta:
       verbose_name_plural="rooms"
    
     
    def __str__(self):
      return(self.name)
    
class Register(models.Model):
   student_id=models.IntegerField(null=True)
   email=models.EmailField(primary_key=True,max_length=155)
   name = models.CharField(max_length=30)
   father_name=models.CharField(max_length=50)
   mother_name=models.CharField(max_length=50 ,null=True,blank=True)
   age=models.IntegerField()
   dob=models.DateField()
   password=models.CharField(max_length=60)
   confirm_password=models.CharField(max_length=60)
   category=models.CharField(max_length=12, choices=CATEGORY_CHOICE, null=True)
   phone_no=models.IntegerField()
   address=models.TextField()


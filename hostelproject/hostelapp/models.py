from django.db import models
import datetime
ROOMTYPE_CHOICE=[
   ('Single bed','Single bed'),
   ('Double bed','Double bed'),
   ('More beds','More beds'),
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
    



from django.db import models

# Create your models here.
class rooms(models.Model):
    name=models.CharField(max_length=20)
    checkin=models.DateField()
    checkout=models.DateField()
    Roomtype=models.CharField(max_length=30)

    class Meta:
       verbose_name_plural="rooms"
    
     
    def __str__(self):
      return(self.name)
    
class roombooking(models.Model):
    userid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=20)
    checkin=models.DateField()
    checkout=models.DateField()
    Roomtype=models.CharField(max_length=30)
    Amount=models.IntegerField()

    class Meta:
       verbose_name_plural="Roombooking"
    
     
    def __str__(self):
      return(self.name)
   


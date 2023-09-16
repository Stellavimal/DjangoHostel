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


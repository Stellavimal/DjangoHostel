from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(rooms)
class roomsAdmin(admin.ModelAdmin):
    list_display=['name','checkin','checkout','Roomtype']


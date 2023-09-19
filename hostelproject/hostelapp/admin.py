from django.contrib import admin
from .models import *
import datetime

# Register your models here.

@admin.register(rooms)
class roomsAdmin(admin.ModelAdmin):
    list_display=['name','checkin','checkout','Roomtype']

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('email','name','father_name','mother_name','category','password')
    search_fields = ['email']

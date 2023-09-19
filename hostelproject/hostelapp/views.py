from django.shortcuts import render
from rest_framework import viewsets
from .models import rooms
from .serializers import roomsSerializer
from .models import Register
from .serializers import RegisterSerializer
# from django_filters import rest_framework as django_filters


# Create your views here.
class roomsViewSet(viewsets.ModelViewSet):
    queryset=rooms.objects.all()
    serializer_class= roomsSerializer
    permission_class=[]
    
class RegisterViewSet(viewsets.ModelViewSet):
    queryset=Register.objects.all()
    serializer_class = RegisterSerializer
    permission_class = []




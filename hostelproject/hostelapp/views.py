from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# from django_filters import rest_framework as django_filters


# Create your views here.
class roomsViewSet(viewsets.ModelViewSet):
    queryset=rooms.objects.all()
    serializer_class= roomsSerializer
    permission_class=[]
class roombookingViewSet(viewsets.ModelViewSet):
    queryset=roombooking.objects.all()
    serializer_class= roombookingSerializer
    permission_class=[]

# Create your views here.

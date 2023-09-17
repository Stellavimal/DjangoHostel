from django.shortcuts import render
from rest_framework import viewsets
from .models import rooms,roombooking
from .serializers import roomsSerializer,roombookingSerializer
# from django_filters import rest_framework as django_filters


# Create your views here.
class roomsViewSet(viewsets.ModelViewSet):
    queryset=rooms.objects.all()
    serializer_class= roomsSerializer
    permission_class=[]



# Create your views here.

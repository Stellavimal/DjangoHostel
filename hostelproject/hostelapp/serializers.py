from rest_framework import serializers
from .models import *
# from .models import Register


class roomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=rooms
        fields="__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields="__all__"

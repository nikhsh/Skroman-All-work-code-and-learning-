from attr import fields
from yaml import serialize
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id','F_Name','L_Name','E_Mail','Password','Create_Password','Mobile_No','Art_Type')


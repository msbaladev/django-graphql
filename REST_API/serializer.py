from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields=['name','image','price','quantity']
        


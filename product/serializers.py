from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    name= serializers.CharField(required=False)
    category= serializers.CharField(required=False)
    price= serializers.FloatField(required=False)

    class Meta:
        model= Product
        fields =['id', 'name', 'category', 'price']
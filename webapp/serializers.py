from django.db.models import fields
from rest_framework import serializers
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from .models import Products

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductFilter(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['category', 'brand', 'source', 'subcategory']
        
             
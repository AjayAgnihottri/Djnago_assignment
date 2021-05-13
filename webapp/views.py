from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django_filters import filterset
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Products
from .serializers import ProductFilter, productSerializers
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

class productList(APIView):
    @api_view(['GET'])
    def getProductByPk(request,pk):
        products = Products.objects.get(urlh = pk)
        serializer = productSerializers(products)
        return Response(serializer.data)


    @api_view(['GET'])
    def getProducts(request):
        products = Products.objects.all()
        serializer = productSerializers(products, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def getProductsByTitle(request, title):
        products = Products.objects.filter(title = title)
        serializer = productSerializers(products, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def getProductsBySku(request, sku):
        products = Products.objects.filter(sku = sku)
        serializer = productSerializers(products, many=True)
        return Response(serializer.data)    
    
    @api_view(['GET'])
    def getProductsBySku(request, sku):
        products = Products.objects.filter(sku = sku)
        serializer = productSerializers(products, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def updateProduct(request, pk):
        product = Products.objects.get(urlh = pk)
        serializer = productSerializers(instance = product, data = request.data)

        if serializer .is_valid():
            serializer.save()

        return Response(serializer.data)
    

class ProductFilterList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = productSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'source', 'subcategory']

class ProductSearchList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = productSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title', 'sku']


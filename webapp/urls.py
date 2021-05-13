from django.urls import path
from rest_framework import views
from .models import Products
from webapp import views


urlpatterns = [
path('fetchAll', views.productList.getProducts, name='ProductsList'),
path('fetchByTitle/', views.ProductSearchList.as_view()),
path('updateProduct/<str:pk>',views.productList.updateProduct, name='Update Product'),
path('fetchProductByPk/<str:pk>', views.productList.getProductByPk, name = 'fetch'),
path('filterProducts/',views.ProductFilterList.as_view()),
]

from django.shortcuts import render
from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer


class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer
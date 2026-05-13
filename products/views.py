from django.shortcuts import render
from django.views import View
from .models import Product
from django.views.generic import DetailView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer


class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'produits'


class ProductDetailsView(DetailView):
    template_name = "products/product_detail.html"
    model = Product
    context_object_name = 'product'


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
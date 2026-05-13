from django.urls import path
from .views import ProductDetailsView, ProductsListView, ProductList, ProductDetail

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product_detail'),
    path('api/products/', ProductList.as_view(), name='api_product_list'),
    path('api/products/<int:pk>', ProductDetail.as_view(), name='api_product_detail'),
]
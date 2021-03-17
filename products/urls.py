from django.urls import path
from .views import products_list, products_details, products_add, products_edit
urlpatterns = [
    path('products/', products_list, name = 'products_list'),
    path('products/add', products_add, name = 'products_add'),
    path('products/<pk>', products_details, name='products_details'),
    path('products/edit/<pk>', products_edit, name='products_edit')
]
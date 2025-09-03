
from django.urls import path
from .views import product_details_view, product_create_view, product_edit_view,product_view

app_name = 'shop'

urlpatterns = [
    path('product/', product_view, name='products'),
    path('product/<int:my_id>/', product_details_view, name='productdetails'),
    path('product/create/', product_create_view, name='product_create_view'),
    path('product/edit/', product_edit_view, name='product_edit_view'),
]
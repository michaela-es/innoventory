from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/modal/', views.product_add_modal, name='product_add_modal'),
    path('add/', views.add_product, name='add_product'),
]

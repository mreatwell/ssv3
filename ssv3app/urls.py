# ssv3app/urls.py
from django.urls import path
from ssv3app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('items/create/', views.create_item, name='create_item'),
]

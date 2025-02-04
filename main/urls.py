# UkrKraft_2025_name='main'
from django.urls import path
from django.contrib import admin
from main import views

app_name = 'main'  # Визначення простору імен

urlpatterns = [
    path('', views.index, name='index'),

     path('about/', views.about, name='about'),
     path('delivery_payment/', views.delivery_payment, name='delivery_payment'),
     path('contacts/', views.contacts, name='contacts'),
]

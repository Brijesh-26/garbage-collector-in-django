from django.contrib import admin
from django.urls import path, include
from gbapp import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact)
]

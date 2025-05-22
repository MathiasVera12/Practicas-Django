from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.nueva_tarea, name='create'),
    path('list/', views.listar, name='list')
]
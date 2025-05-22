from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.index, name='list'),
    path('notes/create/', views.new_note, name='create'),

]
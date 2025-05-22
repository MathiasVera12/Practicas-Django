from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')

def nueva_tarea(request):
    return render(request, 'todoapp/form.html')

def listar(request):
    return render(request, 'todoapp/lista.html')
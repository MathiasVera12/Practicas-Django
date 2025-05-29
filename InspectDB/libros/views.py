from rest_framework import viewsets
from .models import Autores, Libros
from .serializers import AutoresSerializer, LibrosSerializer

# Create your views here.
class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer
    
class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer
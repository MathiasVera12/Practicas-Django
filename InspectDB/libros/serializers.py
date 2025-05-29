from rest_framework import serializers
from .models import Autores, Libros

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'
        read_only_fields = ('id',)
        
class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'
        read_only_fields = ('id',)
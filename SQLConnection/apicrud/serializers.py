from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','lastname', 'age', 'address','created_at')
        read_only_fields = ('id','created_at')
        
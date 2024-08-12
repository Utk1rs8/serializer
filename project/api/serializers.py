from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    city= serializers.CharField(max_length=100)
    roll= serializers.IntegerField()

class StudentSerializer(serializers.Serializer):
    class Meta:
        model=Student
        fields=["id","name","city","roll"]
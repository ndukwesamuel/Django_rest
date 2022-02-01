from rest_framework import serializers
from .models import CareerModle

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerModle
        fields = '__all__'
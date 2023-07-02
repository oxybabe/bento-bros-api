from rest_framework import serializers

from .models import Appetizer, Dessert, MainCourse

class AppetizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appetizer
        fields= '__all__'
    
class MainCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCourse
        fields = '__all__'
    
class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert    
        fields = '__all__'
    
    
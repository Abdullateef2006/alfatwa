from .models import *
from rest_framework import serializers


class lectureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lecture
        fields = '__all__'
        
class episodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Episodes
        # fields = '__all__'
        fields = ['video','audio', 'title','lecture']
        
        
class questionserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Questions
        fields = ['question','answer',]
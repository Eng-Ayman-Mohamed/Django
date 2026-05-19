from rest_framework import serializers
from .models import trainee

class traineeSerializer(serializers.ModelSerializer):

    class Meta : 
        model = trainee
        fields = [
                'id',  
                'firstName', 
                'lastName', 
                'numOfMonths', 
                'track', 
                'createdAt', 
                'image', 
                'course'
            ]
            
        read_only_fields = ['id', 'createdAt']
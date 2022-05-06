from rest_framework import serializers
from app1.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','text','author']
        
        ordering=['-text']
        read_only_field=['id','pk','added_text']
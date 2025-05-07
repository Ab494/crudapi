from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'owner']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password']
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
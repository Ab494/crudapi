from os import name
from drf_yasg.utils import swagger_auto_schema
from re import search
from warnings import filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.decorators import method_decorator


from rest_framework import viewsets
from . models import Task 
from . serializers import TaskSerializer, RegisterSerializer, UserSerializer, UserProfileSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description = "List all tasks.", tags=["Tasks"]
))

@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Create a new task.", tags=['Tasks']
))
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['title', 'description']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
@swagger_auto_schema(
    operation_description="Register a new user with username, email and password.",
    tags = ['User Registration'] 
)
class RegisterView(generics.CreateAPIView):
    queryset =User.objects.all()
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

   
@swagger_auto_schema(
    method = 'get',
    operation_description= "Get details of the logged-in user.",
    tags = ['User Profile']
)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'patch']
    def get_object(self):
        return self.request.user
 

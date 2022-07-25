# from django.shortcuts import render
from common.serializer import UserSerializer
from rest_framework import generics
from common.models import User
# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
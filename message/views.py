from urllib import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from message.serializer import CHatSerializer, MessageSerializer, MessagePostSerializer 
from message.models import Chat, Message

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ChatListApiView(generics.ListAPIView):
    # queryset = Chat.objects.all()
    serializer_class = CHatSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        user = self.request.user
        return Chat.objects.filter(members = user)
    

class MessageListApiView(generics.ListCreateAPIView):
    # queryset = Chat.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        user = self.request.user
        chat = Chat.objects.get(members=user)
        
        return Message.objects.filter(chat = chat)
    
    def post(self, request):
        serializer = MessagePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageCreateApiView(generics.CreateAPIView):
    # queryset = Chat.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    

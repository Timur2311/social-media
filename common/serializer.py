from dataclasses import fields

from rest_framework import serializers
from message.models import Chat, Message
from common.models import User


        
        
        
class UserSerializer():    
    class Meta:
        model = User
        fields = ('email', 'password')
        
        


from dataclasses import fields
from urllib import request
from wsgiref import validate
from rest_framework import serializers
from message.models import Chat, Message
from common.models import User

class CHatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        
class MessageSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     if not Chat.objects.filter(members = request.user):
    #         raise serializers.ValidationError('This field must be an even number.')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Message
        fields = "__all__"
        
        
        
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = "__all__"
        
        

class MessagePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Message
        fields = "__all__"
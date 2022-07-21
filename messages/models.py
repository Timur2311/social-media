from turtle import ondrag
from django.db import models

from common.models import Profile

class Message(models.Model):
    from_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    content = models.TextField(max_length=4096)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message)  
    
    
    

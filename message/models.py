from tkinter import ON
from django.db import models
from common.models import User

HALF_HOUR = "30 minutes"
ONE_HOUR = "1 soat"
TEN_HOUR = "10 soat"
ONE_DAY = "24 soat"
USER_CHOICE = "Xohlaganimda yoqaman"
MUTE_CHOICES = (
    (HALF_HOUR, "30 minutes"),
    (ONE_HOUR, "1 soat"),
    (TEN_HOUR, "10 soat"),
    (ONE_DAY, "24 soat"),
    (USER_CHOICE, "Xohlaganimda yoqaman"),
)


class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_owner")
    members = models.ManyToManyField(User)
    mute_for = models.CharField(max_length=64, choices=MUTE_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def create_message(self,content):
        message = Message.objects.create(chat=self,content = content)
        return message
    
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField(max_length=4096)    
    is_read = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
        
    
    

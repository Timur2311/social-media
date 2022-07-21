from post.models import Post, FRIENDS
from common.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.type == FRIENDS:
        instance.visible_for_users.add(kwargs['friend'])
        
        


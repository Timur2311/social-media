
from django.db import models
from common.models import User




PUBLIC = "Public"
ONLY_ME = "Only_me"
FRIENDS = "Friends"
POST_TYPE = (
    (PUBLIC, "Public"),
    (ONLY_ME, "Only_me"),
    (FRIENDS, "Friends"),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "post_images/")
    file = models.FileField(upload_to = "post_files/")
    content = models.TextField()
    shares_count = models.PositiveIntegerField(default=0)
    
    

    type = models.CharField(max_length=64, choices=POST_TYPE)
    visible_for_users = models.ManyToManyField(User, related_name="visible_profiles", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
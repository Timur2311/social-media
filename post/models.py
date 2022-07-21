
from django.db import models
from common.models import Profile



PUBLIC = "Public"
ONLY_ME = "Only_me"
FRIENDS = "Friends"
POST_TYPE = (
    (PUBLIC, "Public"),
    (ONLY_ME, "Only_me")
    (FRIENDS, "Friends"),
)


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "post_images/")
    file = models.FileField(upload_to = "post_files/")
    content = models.TextField()
    shares_count = models.PositiveIntegerField(default=0)
    

    type = models.CharField(max_length=64, choices=POST_TYPE)
    visible_for_profiles = models.ManyToManyField(Profile, related_name="visible_profiles")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

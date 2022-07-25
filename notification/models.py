

from django.db import models

from common.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from post.models import Post


COMMENT = "Comment"
FOLLOW = "Follow"
LIKE = "Like"
SHARE = "Share"
ADD = "Add"
NOTIFICATION_CHOICES = (
    (COMMENT, "Comment"),
    (FOLLOW, "Follow"),
    (LIKE, "Like"),
    (SHARE, "Share"),
    (ADD, "Add"),
)







class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=64, choices=NOTIFICATION_CHOICES)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    is_read = models.BooleanField(default=False)

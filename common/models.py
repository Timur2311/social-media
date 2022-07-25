# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token

from post.models import Post


MALE = "Erkak"
FEMALE = "Ayol"
GENDER_CHOICES = (
    (MALE, "Erkak"),
    (FEMALE, "Ayol")
)


class Language(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=4096)


class User(AbstractUser):
    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        }
    )
    slug = models.CharField(max_length=4096, null=True)
    avatar = models.ImageField(upload_to="profile_photos/", null=True)
    cover_photo = models.ImageField(upload_to="profile_cpvers/")
    bio = models.TextField(max_length=4096, null=True)
    job = models.CharField(max_length=4096, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=128, null=True)

    followers = models.ManyToManyField('self')
    followings = models.ManyToManyField('self')
    blocked_users = models.ManyToManyField('self')

    followers_number = models.PositiveIntegerField(default=0)
    followings_number = models.PositiveIntegerField(default=0)

    is_online = models.BooleanField(default=False)
    was_active_at = models.DateTimeField(null=True)

    website = models.CharField(max_length=128, null=True)
    facebook_link = models.CharField(max_length=128, null=True)
    twitter_link = models.CharField(max_length=128, null=True)
    instagram_link = models.CharField(max_length=128, null=True)

    language = models.ForeignKey(
        "Language", on_delete=models.CASCADE, null=True, blank=True)
    
    shared_posts = models.ManyToManyField(Post)

    created_at = models.DateTimeField(
        ("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    # SETTINGS
    # USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    # REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def get_friends(self):
        followers = set(self.followers)
        followings = set(self.followings)
        return followers.intersection(followings)
    
    def get_last_followers(self):
        number_of_followers = self.followers.all().count()
        if number_of_followers > self.followers_number:
            diff = number_of_followers -  self.followers_number
            return self.followers.all()[:diff]
        
    
    
    from django.conf import settings
    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from rest_framework.authtoken.models import Token

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            print("kirdi")
            Token.objects.create(user=instance)
        return redirect("/api-token-auth/")

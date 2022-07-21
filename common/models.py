# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models



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
    slug = models.CharField(max_length=4096)
    avatar = models.ImageField(upload_to = "profile_photos/")
    cover_photo = models.ImageField(upload_to="profile_cpvers/")
    bio = models.TextField(max_length=4096)
    job = models.CharField(max_length=4096)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)  
    location = models.CharField(max_length=128)
       
    followers = models.ManyToManyField('self', related_name="followers")
    following = models.ManyToManyField('self', related_name="followings")
    blocked_users = models.ManyToManyField('self', related_name="blocked_users")

    
    followers_number = models.PositiveIntegerField(default=0)
    followings_number = models.PositiveIntegerField(default=0)
    
    is_online = models.BooleanField(default=False)
    was_active_at = models.DateTimeField()
    
    website = models.CharField(max_length=128)
    facebook_link = models.CharField(max_length=128)
    twitter_link = models.CharField(max_length=128)
    instagram_link = models.CharField(max_length=128)
    
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    
    
    created_at = models.DateTimeField(("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    # SETTINGS
    USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")




    
    

    
    
    
    

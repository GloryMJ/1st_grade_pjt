from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from .presents import CustomUserManager

def user_image_path(instance, filename):
    return f'profile/{instance.email.strip().rsplit("@", 1)[0]}/{filename}'

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address") ,max_length=100, unique=True)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    location = models.TextField(blank=True)
    gender = models.IntegerField(default=0)
    image = models.ImageField(blank=True, upload_to=user_image_path)
    age_group = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname', 'gender' ]

    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email

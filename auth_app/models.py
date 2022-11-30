import os
from django.db import models

from config import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'profiles/{instance.id}.{ext}'
    if os.path.exists(f'{settings.MEDIA_ROOT}/{path}'):
        os.remove(f'{settings.MEDIA_ROOT}/{path}')
    return path


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        _('email address'), max_length=254, unique=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    display_photo = models.ImageField(
        upload_to=user_directory_path, blank=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


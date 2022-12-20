import os
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
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
    display_photo = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, _("Male")
        FEMALE = 2, _("Female")
        OTHER = 3, _("Other")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField(
        choices=Gender.choices, default=Gender.FEMALE)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
import uuid

from config import settings

# Create your models here.


def service_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'services/{instance.slug}.{ext}'
    if os.path.exists(f'{settings.MEDIA_ROOT}/{path}'):
        os.remove(f'{settings.MEDIA_ROOT}/{path}')
    return path

class Service(models.Model):
    name = models.CharField(_("Name"), max_length=256)
    description = models.TextField(_("Description"), blank=True)
    image = models.FileField(upload_to=service_directory_path, blank=True)
    slug = models.SlugField(_("Safe Url"), unique=True, blank=True, null=True)
    created_on = models.DateField(_("Created on"), default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.name)}"

        self.name = self.name

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


def package_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'packages/{instance.slug}.{ext}'
    if os.path.exists(f'{settings.MEDIA_ROOT}/{path}'):
        os.remove(f'{settings.MEDIA_ROOT}/{path}')
    return path


class Package(models.Model):
    name = models.CharField(_("Name"), max_length=256)
    duration = models.IntegerField(_("Duration"))
    price = models.IntegerField(_("Price"))
    description = models.TextField(_("Description"), blank=True)
    image = models.FileField(upload_to=package_directory_path, blank=True)
    slug = models.SlugField(_("Safe Url"), unique=True, blank=True, null=True)
    created_on = models.DateField(_("Created on"), default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.name)}"

        self.name = self.name

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"

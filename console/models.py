from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone

from auth_app.models import User
from website.models import Package

# Create your models here.


class Appointment(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    package = models.ForeignKey(Package, verbose_name=_("Package"), on_delete=models.CASCADE)
    datetime = models.DateTimeField(_("Date and Time"), max_length=256, blank=True)
    created_on = models.DateField(_("Created on"), default=timezone.now)


    def __str__(self) -> str:
        return f"{self.datetime}"

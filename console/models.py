from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone

from auth_app.models import User
from website.models import Package

# Create your models here.


class Appointment(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1, _("Pending")
        APPROVED = 2, _("Approved")
        CANCELLED = 3, _("Cancelled")

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    package = models.ForeignKey(Package, verbose_name=_("Package"), on_delete=models.CASCADE)
    datetime = models.DateTimeField(_("Date and Time"), max_length=256, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
    created_on = models.DateField(_("Created on"), default=timezone.now)


    def __str__(self) -> str:
        return f"{self.datetime}"


class BraintreeCustomer(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    customer_id = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user.__str__()}"


class BraintreeTransaction(models.Model):
    class Source(models.IntegerChoices):
        SESSION = 1, _("Session")
        DONATION = 2, _("Donation")

    customer = models.ForeignKey(BraintreeCustomer, on_delete=models.CASCADE, related_name='transactions')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    source = models.IntegerField(
        choices=Source.choices, default=Source.SESSION)
    created_on = models.DateField(_("Created on"), default=timezone.now)

    def __str__(self) -> str:
        return f"{self.transaction_id}"

from django.contrib import admin

from console.models import Appointment

# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'datetime')

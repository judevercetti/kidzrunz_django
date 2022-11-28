from django.contrib import admin

from website.models import Package, Service

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')

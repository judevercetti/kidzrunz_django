from django.contrib import admin

from website.models import Service

# Register your models here.

@admin.register(Service)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

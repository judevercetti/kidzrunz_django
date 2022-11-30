from django.contrib import admin

from auth_app.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):

        fieldsets = (
            *UserAdmin.fieldsets,
            (
                'Basic Information',
                {
                    'fields': (
                        'phone_number',
                        'display_photo',
                    ),
                },
            ),
        )
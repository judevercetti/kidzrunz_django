from django.contrib import admin

from auth_app.models import Profile, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

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

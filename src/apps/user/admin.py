from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = (
        'username',
        'full_name',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'password',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'username',
                    'full_name',
                    'groups',
                ),
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
                'username',
                'full_name',
                'groups',
            ),
        }),
    )
    list_display = (
        'id',
        'username',
    )
    ordering = ('-id',)

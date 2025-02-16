from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from app_users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'role', 'preferred_language',
        'language_level', 'bio', 'level', 'is_active', 'is_staff'
    )
    list_filter = ('role', 'preferred_language', 'language_level', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date', 'phone_number')}),
        ('Permissions',
         {'fields': ('role', 'preferred_language', 'language_level', 'bio', 'level', 'is_active', 'is_staff')}),
    )

    ordering = ('-id',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)

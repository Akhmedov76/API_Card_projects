from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from app_users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id', 'email', 'full_name', 'birth_date', 'phone_number', 'role', 'preferred_language',
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
admin.site.site_header = _("Card Admin")
admin.site.site_title = _("My Admin")
admin.site.index_title = _("Welcome Admin Dashboard")

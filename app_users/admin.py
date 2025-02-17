from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'role')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'birth_date', 'phone_number', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role', 'preferred_language', 'language_level')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
    )


admin.site.unregister(Group)
admin.site.site_header = _("Card Admin")
admin.site.site_title = _("My Admin")
admin.site.index_title = _("Welcome Admin Dashboard")

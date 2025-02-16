from django.contrib import admin

from app_notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'message', 'timestamp', 'is_read')
    list_filter = ('user', 'timestamp', 'is_read')
    search_fields = ('user__email', 'title', 'message')
    ordering = ('-id',)
    fields = ('user', 'title', 'message', 'timestamp', 'is_read')


admin.site.register(Notification, NotificationAdmin)
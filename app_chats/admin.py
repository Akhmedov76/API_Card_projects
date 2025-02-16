from django.contrib import admin

from app_chats.models import Chat


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message', 'timestamp', 'is_read')
    list_filter = ('sender', 'receiver', 'timestamp', 'is_read')
    search_fields = ('sender__email', 'receiver__email', 'message')
    ordering = ('-id',)
    fields = ('sender', 'receiver', 'message', 'timestamp', 'is_read')


admin.site.register(Chat, ChatAdmin)

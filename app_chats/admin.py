from django.contrib import admin
from .models import Chat, ChatMessage

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2', 'created_at')
    search_fields = ('user1', 'user2')
    ordering = ('-created_at',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'sender', 'short_message', 'file', 'created_at')
    search_fields = ('message', 'sender__username', 'chat__user1', 'chat__user2')
    ordering = ('-created_at',)

    def short_message(self, obj):
        return obj.message[:30] + ('...' if len(obj.message) > 30 else '')
    short_message.short_description = 'Message'

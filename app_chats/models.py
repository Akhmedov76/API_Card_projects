from django.db import models

from app_users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Yangilangan vaqt")

    class Meta:
        abstract = True


class Chat(BaseModel):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_started')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_received')


    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


class ChatMessage(BaseModel):
    message = models.TextField()
    file = models.FileField(upload_to="message_file/", blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')

    class Meta:
        verbose_name = 'ChatMessage'
        verbose_name_plural = 'ChatMessages'

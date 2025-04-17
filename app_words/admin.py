from django.contrib import admin
from .models import WordCard, PrivateCard

@admin.register(WordCard)
class WordCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translation', 'team', 'created_at', 'updated_at')
    list_filter = ('team',)
    search_fields = ('word', 'translation')
    ordering = ('-created_at',)


@admin.register(PrivateCard)
class PrivateCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translation', 'user', 'status', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('word', 'translation', 'description')
    ordering = ('-created_at',)

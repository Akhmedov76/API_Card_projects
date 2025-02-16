from django.contrib import admin

from app_words.models import WordCard, PrivateCard


class WordCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translation', 'example', 'team')
    list_filter = ('team',)
    search_fields = ('word', 'translation', 'example')
    ordering = ('-id',)
    fields = ('word', 'translation', 'example', 'team')


class PrivateCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translation', 'description', 'user')
    list_filter = ('user',)
    search_fields = ('word', 'translation', 'description')
    ordering = ('-id',)
    fields = ('word', 'translation', 'description', 'user')


admin.site.register(WordCard, WordCardAdmin)
admin.site.register(PrivateCard, PrivateCardAdmin)
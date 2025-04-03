from django.contrib import admin

from app_games.models import MiniGame


class MiniGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_type', 'team', 'results', 'created_at', 'updated_at', 'is_completed', 'is_winner', 'winner', 'loser')
    list_filter = ('team', 'created_at', 'updated_at', 'is_completed', 'is_winner')
    search_fields = ('game_type', 'team__name', 'results')
    ordering = ('-id',)
    fields = ('game_type', 'team', 'results',  'is_completed', 'is_winner', 'winner', 'loser')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(MiniGame, MiniGameAdmin)
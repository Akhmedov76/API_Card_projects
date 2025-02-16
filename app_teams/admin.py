from django.contrib import admin

from app_teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('members',)
    search_fields = ('name', 'members__email')
    ordering = ('-id',)
    fields = ('name', 'members',)


admin.site.register(Team, TeamAdmin)
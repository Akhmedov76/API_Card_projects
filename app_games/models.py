from django.db import models

from app_teams.models import Team


class MiniGame(models.Model):
    game_type = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='mini_games')
    results = models.TextField()

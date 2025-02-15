from django.db import models

from app_teams.models import Team


class WordCard(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='word_cards')
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

from app_teams.models import Team


class MiniGame(models.Model):
    game_type = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='mini_games')
    results = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winning_mini_games', null=True)
    loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='losing_mini_games', null=True)

    def __str__(self):
        return f'{self.game_type} - {self.team.name}'

    class Meta:
        verbose_name = 'Mini Game'
        verbose_name_plural = 'Mini Games'

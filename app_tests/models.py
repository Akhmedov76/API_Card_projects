from django.db import models
from app_teams.models import Team


class Test(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tests')
    questions = models.TextField()
    answers = models.TextField()

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'
        ordering = ['-id']

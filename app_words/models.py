from django.db import models

from app_teams.models import Team
from app_users.models import User


class WordCard(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='word_cards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Word Card'
        verbose_name_plural = 'Word Cards'


class PrivateCard(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_cards')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Private Card'
        verbose_name_plural = 'Private Cards'

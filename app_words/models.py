from django.db import models

from app_teams.models import Team
from app_users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WordCard(BaseModel):

    STATUS_CHOICES = [
        ('to_learn', 'To Learn'),
        ('known', 'Known'),
        ('learned', 'Learned'),
    ]


    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_learn')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='word_cards')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Word Card'
        verbose_name_plural = 'Word Cards'


class PrivateCard(BaseModel):

    STATUS_CHOICES = [
        ('to_learn', 'To Learn'),
        ('known', 'Known'),
        ('learned', 'Learned'),
    ]


    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_learn')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_cards')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Private Card'
        verbose_name_plural = 'Private Cards'

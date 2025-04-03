"""

"""

from django.db import models
from app_users.models import User


class Team(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_teams",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class JoinRequest(models.Model):
    status_choices = [
        ("APROVED", "Aproved"),
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
    ]
    user = models.ForeignKey(
        User, related_name="join_requests",
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team, related_name="requests",
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=status_choices,
        default="PENDING"
    )
    
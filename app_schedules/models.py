from django.db import models

from app_users.models import User
from app_words.models import WordCard


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    word_card = models.ForeignKey(WordCard, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.first_name} - {self.word_card.word}'

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    purpose = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    feedback = models.TextField(blank=True, null=True)
    confirmation_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} - {self.appointment_date}'

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    date_of_birth = models.DateField()
    language_preference = models.CharField(max_length=20, choices=[('Lang1', 'Lang1'), ('Lang2', 'Lang2')], default='Lang1')

    def __str__(self):
        return self.username


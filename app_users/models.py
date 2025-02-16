from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Sorry, you have to do it via email!!!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    LANGUAGE_CHOICES = [
        # ('uz', 'Uzbek'),
        # ('ru', 'Russian'),
        ('en', 'English'),
    ]

    LANGUAGE_LEVEL_CHOICES = [
        ('A1', 'Beginner'),
        ('A2', 'Elementary'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper-Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficient'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[('user', 'User'), ('admin', 'Admin')])
    preferred_language = models.CharField(
        max_length=50, choices=LANGUAGE_CHOICES, blank=True, null=True
    )
    language_level = models.CharField(
        max_length=2, choices=LANGUAGE_LEVEL_CHOICES, blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

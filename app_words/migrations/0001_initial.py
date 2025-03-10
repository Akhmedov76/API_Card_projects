# Generated by Django 5.1.1 on 2025-02-16 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_cards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Private Card',
                'verbose_name_plural': 'Private Cards',
            },
        ),
        migrations.CreateModel(
            name='WordCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('example', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_cards', to='app_teams.team')),
            ],
            options={
                'verbose_name': 'Word Card',
                'verbose_name_plural': 'Word Cards',
            },
        ),
    ]

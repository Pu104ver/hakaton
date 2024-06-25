# Generated by Django 5.0.6 on 2024-06-11 18:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_participant',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('organizer', 'Организатор'), ('moderator', 'Модератор'), ('user', 'Пользователь'), ('guest', 'Гость')], default='user', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sphere_of_activity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

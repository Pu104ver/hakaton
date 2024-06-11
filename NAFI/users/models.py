from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('organizer', 'Организатор'),
        ('moderator', 'Модератор'),
        ('user', 'Пользователь'),
        ('guest', 'Гость'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    sphere_of_activity = models.CharField(max_length=255, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

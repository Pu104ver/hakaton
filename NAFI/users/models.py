from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=False)

from django.db import models
from django.conf import settings

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='meetings_participants')

    def __str__(self):
        return self.title

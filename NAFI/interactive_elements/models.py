from django.db import models

class InteractiveElement(models.Model):
    ELEMENT_TYPES = [
        ('poll', 'Poll'),
        ('quiz', 'Quiz'),
        ('survey', 'Survey'),
        ('qna', 'Q&A'),
    ]

    title = models.CharField(max_length=255)
    element_type = models.CharField(max_length=50, choices=ELEMENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

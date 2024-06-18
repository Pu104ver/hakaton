from django.db import models
from django.conf import settings
from meetings.models import Meeting


class Interactive(models.Model):
    INTERACTIVE_TYPES = [
        ('text_question', 'Открытый вопрос (текст)'),
        ('number_question', 'Открытый вопрос (число)'),
        ('audience_qa', 'Audience Q&A'),
        ('networking', 'Нетворкинг'),
        ('star_voting', 'Экспресс-голосование (звёздочки)'),
        ('single_choice', 'Экспресс-голосование (Single-choice)'),
        ('multiple_choice', 'Экспресс-голосование (Multiple choice)'),
        ('survey', 'Опрос по небольшой анкете'),
        ('quiz', 'Викторина'),
    ]
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='interactives')
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=INTERACTIVE_TYPES)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_repeatable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TextQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='text_question')
    question_text = models.TextField(blank=True, default='') 
    max_length = models.PositiveIntegerField(default=1000)

class NumberQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='number_question')
    question_text = models.TextField(blank=True, default='')
    min_value = models.FloatField(default=0)
    max_value = models.FloatField(default=100)

class AudienceQA(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='audience_qa')
    question_text = models.TextField(blank=True, default='')
    
class Networking(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='networking')
    description = models.TextField(blank=True, default='')
    session_duration = models.PositiveIntegerField(default=5)  # Duration in minutes

class StarVoting(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='star_voting')
    question_text = models.TextField(blank=True, default='')
    max_stars = models.PositiveIntegerField(default=5)

class SingleChoice(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='single_choice')
    question_text = models.TextField(blank=True, default='')
    options = models.JSONField()  # List of options

class MultipleChoice(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='multiple_choice')
    question_text = models.TextField(blank=True, default='')
    options = models.JSONField()  # List of options

class Survey(models.Model):
    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE, related_name='survey')
    questions = models.JSONField()  # List of questions

class Quiz(models.Model):
    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE, related_name='quiz')
    questions = models.JSONField()  # List of questions with correct answers

class InteractiveResponse(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    response = models.JSONField()  # Store the response data in JSON format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

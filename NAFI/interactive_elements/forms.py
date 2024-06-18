from django import forms
from django.forms import Textarea, NumberInput, TextInput, Select
from .models import (Interactive, InteractiveResponse, TextQuestion, NumberQuestion, 
                     AudienceQA, Networking, StarVoting, SingleChoice, MultipleChoice, Survey, Quiz)

class InteractiveForm(forms.ModelForm):
    class Meta:
        model = Interactive
        fields = ('title', 'type', 'description', 'is_active', 'is_repeatable')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_active': forms.CheckboxInput(),
            'is_repeatable': forms.CheckboxInput(),
        }

class TextQuestionForm(forms.ModelForm):
    class Meta:
        model = TextQuestion
        fields = ('question_text', 'max_length')
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'max_length': NumberInput(attrs={'class': 'form-control'}),
        }

class NumberQuestionForm(forms.ModelForm):
    class Meta:
        model = NumberQuestion
        fields = ('question_text', 'min_value', 'max_value')
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'min_value': NumberInput(attrs={'class': 'form-control'}),
            'max_value': NumberInput(attrs={'class': 'form-control'}),
        }

class AudienceQAForm(forms.ModelForm):
    class Meta:
        model = AudienceQA
        fields = ('question_text',)
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class NetworkingForm(forms.ModelForm):
    class Meta:
        model = Networking
        fields = ('description', 'session_duration')
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'session_duration': NumberInput(attrs={'class': 'form-control'}),
        }

class StarVotingForm(forms.ModelForm):
    class Meta:
        model = StarVoting
        fields = ('question_text', 'max_stars')
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'max_stars': NumberInput(attrs={'class': 'form-control'}),
        }

class SingleChoiceForm(forms.ModelForm):
    class Meta:
        model = SingleChoice
        fields = ('question_text', 'options')
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = MultipleChoice
        fields = ('question_text', 'options')
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('questions',)
        widgets = {
            'questions': Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('questions',)
        widgets = {
            'questions': Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class InteractiveResponseForm(forms.ModelForm):
    class Meta:
        model = InteractiveResponse
        fields = ('response',)
        widgets = {
            'response': Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
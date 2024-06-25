from django import forms
from .models import (
    Interactive, TextQuestion, TextAnswer, NumberQuestion, NumberAnswer,
    AudienceQA, Networking, StarVotingQuestion, StarVote, SingleChoiceQuestion,
    SingleChoiceAnswer, MultipleChoiceQuestion, MultipleChoiceAnswer, Survey,
    SurveyQuestion, SurveyAnswer, Quiz, QuizAnswer
)
from meetings.models import Meeting



from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone


User = get_user_model()


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


# Interactive Form
class InteractiveForm(forms.ModelForm):
    class Meta:
        model = Interactive
        fields = ['meeting', 'title', 'type', 'description', 'is_active', 'is_repeatable', 'participants', 'start_time', 'end_time']

    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    start_time = forms.DateTimeField(widget=DateTimeInput(attrs={'min': timezone.now().isoformat()}))
    end_time = forms.DateTimeField(widget=DateTimeInput(attrs={'min': timezone.now().isoformat()}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(InteractiveForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['participants'].queryset = User.objects.exclude(id=user.id)

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time < timezone.now():
                self.add_error('start_time', "The start time cannot be in the past.")
            if end_time <= start_time:
                self.add_error('end_time', "The end time cannot be earlier (or equal) than the start time.")

        return cleaned_data


# Text Question Forms
class TextQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = TextQuestion
        fields = ['question_text', 'max_length', 'meeting', 'title', 'description']


class TextAnswerForm(forms.ModelForm):
    class Meta:
        model = TextAnswer
        fields = ['question', 'user', 'answer_text']


# Number Question Forms
class NumberQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = NumberQuestion
        fields = ['question_text', 'min_value', 'max_value', 'meeting', 'title', 'description']


class NumberAnswerForm(forms.ModelForm):
    class Meta:
        model = NumberAnswer
        fields = ['question', 'user', 'answer_number']


# Audience QA Form
class AudienceQAForm(forms.ModelForm):
    class Meta:
        model = AudienceQA
        fields = ['interactive', 'question_text']


# Networking Form
class NetworkingForm(forms.ModelForm):
    class Meta:
        model = Networking
        fields = ['interactive', 'description', 'session_duration']


# Star Voting Forms
class StarVotingQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = StarVotingQuestion
        fields = ['question_text', 'max_stars', 'meeting', 'title', 'description']


class StarVoteForm(forms.ModelForm):
    class Meta:
        model = StarVote
        fields = ['question', 'user', 'stars']


# Single Choice Forms
class SingleChoiceQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = SingleChoiceQuestion
        fields = ['question_text', 'meeting', 'title', 'description']


class SingleChoiceAnswerForm(forms.ModelForm):
    class Meta:
        model = SingleChoiceAnswer
        fields = ['question', 'user', 'selected_option']


# Multiple Choice Forms
class MultipleChoiceQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    max_choices = forms.IntegerField(min_value=1, required=True, label='Максимальное количество вариантов')

    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_text', 'meeting', 'title', 'description', 'max_choices']


class MultipleChoiceAnswerForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceAnswer
        fields = ['question', 'user', 'selected_options']


# Survey Forms
class SurveyForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Survey
        fields = ['meeting', 'title', 'description']


class SurveyQuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 1}),
        }


class SurveyAnswerForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswer
        fields = ['question', 'user', 'answer_text']


# Quiz Forms
class QuizForm(forms.ModelForm):
    game_type = forms.ChoiceField(choices=Quiz.GAME_TYPE_CHOICES, required=True)
    questions = forms.JSONField()

    class Meta:
        model = Quiz
        fields = ['game_type', 'questions']


class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer
        fields = ['quiz', 'user', 'answers']

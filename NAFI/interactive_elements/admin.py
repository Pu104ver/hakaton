from django.contrib import admin
from .models import (
    Interactive,
    TextQuestion,
    NumberQuestion,
    AudienceQA,
    Networking,
    StarVoting,
    SingleChoice,
    MultipleChoice,
    Survey,
    Quiz,
    InteractiveResponse
)

class InteractiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'meeting', 'is_active', 'is_repeatable', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('type', 'meeting', 'is_active', 'is_repeatable', 'created_at')

class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'max_length', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class NumberQuestionAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'min_value', 'max_value', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class AudienceQAAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class NetworkingAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'session_duration', 'description')
    search_fields = ('interactive__title', 'description')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class StarVotingAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'max_stars', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class SingleChoiceAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class MultipleChoiceAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'question_text')
    search_fields = ('interactive__title', 'question_text')
    list_filter = ('interactive__meeting', 'interactive__created_at')

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'questions')
    search_fields = ('interactive__title',)
    list_filter = ('interactive__meeting', 'interactive__created_at')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'questions')
    search_fields = ('interactive__title',)
    list_filter = ('interactive__meeting', 'interactive__created_at')

class InteractiveResponseAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'user', 'created_at')
    search_fields = ('interactive__title', 'user__username')
    list_filter = ('interactive__meeting', 'created_at')

admin.site.register(Interactive, InteractiveAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(NumberQuestion, NumberQuestionAdmin)
admin.site.register(AudienceQA, AudienceQAAdmin)
admin.site.register(Networking, NetworkingAdmin)
admin.site.register(StarVoting, StarVotingAdmin)
admin.site.register(SingleChoice, SingleChoiceAdmin)
admin.site.register(MultipleChoice, MultipleChoiceAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(InteractiveResponse, InteractiveResponseAdmin)

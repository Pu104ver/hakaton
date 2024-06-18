from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import (
    Interactive, TextQuestion, NumberQuestion, AudienceQA, Networking,
    StarVoting, SingleChoice, MultipleChoice, Survey, Quiz, InteractiveResponse
)
from .forms import (
    InteractiveForm, TextQuestionForm, NumberQuestionForm, AudienceQAForm, NetworkingForm,
    StarVotingForm, SingleChoiceForm, MultipleChoiceForm, SurveyForm, QuizForm, InteractiveResponseForm
)
from .decorators.user_passes_test_custom import user_passes_test_custom
from meetings.models import Meeting

def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

@user_passes_test_custom(is_organizer)
@login_required
def create_interactive(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    
    if request.method == 'POST':
        interactive_form = InteractiveForm(request.POST)
        if interactive_form.is_valid():
            interactive = interactive_form.save(commit=False)
            interactive.meeting = meeting
            interactive.creator = request.user
            interactive.save()
            return redirect('interactive_detail', interactive.id)
    else:
        interactive_form = InteractiveForm()
    
    return render(request, 'interactive_elements/create_interactive.html', {'interactive_form': interactive_form})

@user_passes_test_custom(is_organizer)
@login_required
def add_text_question(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = TextQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = TextQuestionForm()
    return render(request, 'interactive_elements/add_text_question.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_number_question(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = NumberQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = NumberQuestionForm()
    return render(request, 'interactive_elements/add_number_question.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_audience_qa(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = AudienceQAForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = AudienceQAForm()
    return render(request, 'interactive_elements/add_audience_qa.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_networking(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = NetworkingForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = NetworkingForm()
    return render(request, 'interactive_elements/add_networking.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_star_voting(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = StarVotingForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = StarVotingForm()
    return render(request, 'interactive_elements/add_star_voting.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_single_choice(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = SingleChoiceForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = SingleChoiceForm()
    return render(request, 'interactive_elements/add_single_choice.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_multiple_choice(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = MultipleChoiceForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = MultipleChoiceForm()
    return render(request, 'interactive_elements/add_multiple_choice.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_survey(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = SurveyForm()
    return render(request, 'interactive_elements/add_survey.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def add_quiz(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.interactive = interactive
            question.save()
            return redirect('interactive_detail', interactive.id)
    else:
        form = QuizForm()
    return render(request, 'interactive_elements/add_quiz.html', {'form': form})

@user_passes_test_custom(is_organizer)
@login_required
def interactive_detail(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    return render(request, 'interactive_elements/interactive_detail.html', {'interactive': interactive})

@user_passes_test_custom(is_organizer)
@login_required
def participate_interactive(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    if request.method == 'POST':
        response_form = InteractiveResponseForm(request.POST)
        if response_form.is_valid():
            response = response_form.save(commit=False)
            response.interactive = interactive
            response.participant = request.user
            response.save()
            return redirect('interactive_result', interactive.id)
    else:
        response_form = InteractiveResponseForm()
    return render(request, 'interactive_elements/participate_interactive.html', {'interactive': interactive, 'response_form': response_form})

@user_passes_test_custom(is_organizer)
@login_required
def interactive_result(request, interactive_id):
    interactive = get_object_or_404(Interactive, id=interactive_id)
    responses = InteractiveResponse.objects.filter(interactive=interactive)
    return render(request, 'interactive_elements/interactive_result.html', {'interactive': interactive, 'responses': responses})

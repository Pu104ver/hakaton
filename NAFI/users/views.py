from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from courses.models import Module, UserProgress, UserCourse


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def get_greeting(request):
    current_time = datetime.now()
    current_hour = current_time.hour

    if 6 <= current_hour < 12:
        greeting = 'Доброе утро'
        emoji_path = '/static/img/sunrise.png'
    elif 12 <= current_hour < 18:
        greeting = 'Добрый день'
        emoji_path = '/static/img/sun.png'
    elif 18 <= current_hour < 24:
        greeting = 'Добрый вечер'
        emoji_path = '/static/img/sunset.png'
    else:
        greeting = 'Доброй ночи'
        emoji_path = '/static/img/moon.png'

    return f'{greeting}, {request.user.username} <img src="{emoji_path}" alt="emoji" class="emoji">'

@login_required
def profile(request):
    greeting = get_greeting(request=request)
    user = request.user
    
    user_courses = UserCourse.objects.filter(user=user)
    
    courses_progress = []
    
    for user_course in user_courses:
        course = user_course.course
        total_lessons = 0
        completed_lessons = 0
        
        modules = Module.objects.filter(course=course)
        for module in modules:
            module_total_lessons = module.lessons.count()
            module_completed_lessons = UserProgress.objects.filter(
                user=user, lesson__module=module, completed=True).count()
            
            total_lessons += module_total_lessons
            completed_lessons += module_completed_lessons
        
        if total_lessons > 0:
            progress_percent = int((completed_lessons / total_lessons) * 100)
        else:
            progress_percent = 0
        
        courses_progress.append({
            'course': course,
            'progress_percent': progress_percent
        })
    
    context = {
        'greeting': greeting,
        'courses_progress': courses_progress,
        'user': user
    }
    return render(request, 'users/profile.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Module, Lesson, UserCourse, UserProgress
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_course = None
    if request.user.is_authenticated:
        user_course = course.usercourse_set.filter(user=request.user).first()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'user_course': user_course
    })

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_course, created = UserCourse.objects.get_or_create(user=request.user, course=course)
    return redirect('course_detail', course_id=course.id)

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    user_progress = None
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(lesson=lesson, user=request.user).first()
    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'user_progress': user_progress
    })

@login_required
def user_courses(request):
    user_courses = UserCourse.objects.filter(user=request.user)
    return render(request, 'courses/user_courses.html', {'user_courses': user_courses})

@login_required
def mark_lesson_completed(request, lesson_id):
    if request.user.is_authenticated:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        user_progress, created = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
        if not user_progress.completed:
            user_progress.completed = True
            user_progress.save()

            next_lesson = None
            all_lessons = list(lesson.module.lessons.all())
            current_index = all_lessons.index(lesson)

            if current_index + 1 < len(all_lessons):
                next_lesson = all_lessons[current_index + 1]
            else:
                all_modules = list(lesson.module.course.modules.all())
                current_module_index = all_modules.index(lesson.module)

                if current_module_index + 1 < len(all_modules):
                    next_module = all_modules[current_module_index + 1]
                    next_lesson = next_module.lessons.first()
                    messages.success(request, f'Вы завершили модуль. Переход к следующему модулю {next_module.title}.')
                else:
                    messages.success(request, 'Поздравляем! Вы завершили курс.')

            if next_lesson:
                return redirect('lesson_detail', lesson_id=next_lesson.id)
            else:
                return redirect('course_detail', course_id=lesson.module.course.id)
        else:
            messages.info(request, 'Этот урок уже завершен.')
            return redirect('lesson_detail', lesson_id=lesson.id)
    else:
        return redirect('login')

def unmark_lesson_completed(request, lesson_id):
    if request.user.is_authenticated:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        try:
            user_progress = UserProgress.objects.get(user=request.user, lesson=lesson)
            if user_progress.completed:
                user_progress.completed = False
                user_progress.save()
                messages.success(request, 'Урок отмечен как незавершенный.')
        except UserProgress.DoesNotExist:
            messages.error(request, 'Прогресс по этому уроку не найден.')
        return redirect('lesson_detail', lesson_id=lesson.id)
    else:
        return redirect('login')

def access_denied(request):
    return render(request, 'courses/access_denied.html')
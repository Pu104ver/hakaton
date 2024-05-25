from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/index.html')

@login_required
def dashboard(request):
    # Здесь можно добавить логику для получения данных, которые будут отображены на Dashboard
    # Например, получение информации о пользователе или статистики
    context = {
        'user': request.user,
        # Другие данные
    }
    return render(request, 'home/dashboard.html', context)
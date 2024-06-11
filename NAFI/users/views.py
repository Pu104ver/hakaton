from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

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

def profile(request):
    return render(request, 'users/profile.html')


from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')


from django.shortcuts import render, redirect
from .models import InteractiveElement
from .forms import InteractiveElementForm

def interactive_element_list(request):
    elements = InteractiveElement.objects.all()
    return render(request, 'interactive_elements/interactive_element_list.html', {'elements': elements})

def interactive_element_create(request):
    if request.method == 'POST':
        form = InteractiveElementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interactive_element_list')
    else:
        form = InteractiveElementForm()
    return render(request, 'interactive_elements/interactive_element_form.html', {'form': form})

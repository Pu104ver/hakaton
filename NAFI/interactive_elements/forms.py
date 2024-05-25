from django import forms
from .models import InteractiveElement

class InteractiveElementForm(forms.ModelForm):
    class Meta:
        model = InteractiveElement
        fields = ['title', 'element_type']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    field_of_activity = forms.ChoiceField(choices=[
        ('IT', 'Информационные технологии'),
        ('Маркетинг', 'Маркетинг'),
        ('Производство', 'Производство'),
    ], label='Сфера деятельности')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'field_of_activity']

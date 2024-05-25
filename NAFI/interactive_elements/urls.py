from django.urls import path
from . import views

urlpatterns = [
    path('', views.interactive_element_list, name='interactive_element_list'),
    path('new/', views.interactive_element_create, name='interactive_element_create'),
]

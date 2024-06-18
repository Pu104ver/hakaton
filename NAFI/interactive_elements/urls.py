from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('create/<int:meeting_id>/', views.create_interactive, name='create_interactive'),
    path('<int:interactive_id>/', views.interactive_detail, name='interactive_detail'),
    path('<int:interactive_id>/add_text_question/', views.add_text_question, name='add_text_question'),
    path('<int:interactive_id>/add_number_question/', views.add_number_question, name='add_number_question'),
    path('<int:interactive_id>/add_audience_qa/', views.add_audience_qa, name='add_audience_qa'),
    path('<int:interactive_id>/add_networking/', views.add_networking, name='add_networking'),
    path('<int:interactive_id>/add_star_voting/', views.add_star_voting, name='add_star_voting'),
    path('<int:interactive_id>/add_single_choice/', views.add_single_choice, name='add_single_choice'),
    path('<int:interactive_id>/add_multiple_choice/', views.add_multiple_choice, name='add_multiple_choice'),
    path('<int:interactive_id>/add_survey/', views.add_survey, name='add_survey'),
    path('<int:interactive_id>/add_quiz/', views.add_quiz, name='add_quiz'),
    path('<int:interactive_id>/participate/', views.participate_interactive, name='participate_interactive'),
    path('<int:interactive_id>/results/', views.interactive_result, name='interactive_result'),
    path('error/', TemplateView.as_view(template_name='interactive_elements/error_page.html'), name='error_page'),
]

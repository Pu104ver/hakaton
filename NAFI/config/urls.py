from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('events/', include('events.urls')),
    path('interactive-elements/', include('interactive_elements.urls')),
    path('reports/', include('reports.urls')),
    path('meetings/', include('meetings.urls')),
    path('courses/', include('courses.urls')),
    path('notifications/', include('notifications.urls')),
    path('departments/', include('departments.urls')),
]
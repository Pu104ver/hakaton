from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/user_notifications.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    if notification:
        notification.read = True
        notification.save()
    return redirect('user_notifications')

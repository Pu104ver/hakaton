from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .forms import MeetingForm
import requests

@login_required
def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            response = requests.post(
                'https://api.daily.co/v1/rooms',
                headers={
                    'Authorization': f'Bearer {settings.DAILY_CO_API_KEY}',
                    'Content-Type': 'application/json'
                },
                json={
                    'properties': {
                        'enable_chat': True,
                        'enable_screenshare': True,
                        'start_video_off': True,
                        'start_audio_off': True,
                        'enable_people_ui': True,
                        'enable_prejoin_ui': True,
                        'enable_network_ui': True,
                        'enable_emoji_reactions': True,
                        'enable_hand_raising': True,
                        'enable_knocking': True
                    }
                }
            )
            data = response.json()
            meeting_url = data['url']

            meeting = form.save(commit=False)
            meeting.url = meeting_url
            meeting.host = request.user
            meeting.save()
            return redirect('meeting_detail', meeting_id=meeting.id)
    else:
        form = MeetingForm()
    return render(request, 'meetings/create_meeting.html', {'form': form})

def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})

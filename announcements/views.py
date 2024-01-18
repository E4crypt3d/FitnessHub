from django.shortcuts import render
from .models import Announcement

# Create your views here.


def announcements(request):
    exercises = Announcement.workout.all().order_by('-added_at')
    schedules = Announcement.schedules.all().order_by('-added_at')
    ddp = Announcement.ddp.all().order_by('-added_at')
    context = {'specials': exercises, 'schedules': schedules, 'ddp': ddp}
    return render(request, 'announcements.html', context)

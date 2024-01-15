from django.shortcuts import render
from .models import Announcement

# Create your views here.


def announcements(request):
    exercises = Announcement.workout.all()
    schedules = Announcement.schedules.all()
    print(exercises)
    ddp = Announcement.ddp.all()
    context = {'specials': exercises, 'schedules': schedules, 'ddp': ddp}
    return render(request, 'announcements.html', context)

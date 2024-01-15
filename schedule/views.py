from django.shortcuts import render
from .models import Schedule
from . import views
# Create your views here.


def schedule(request):
    schedules = Schedule.objects.all()
    context = {'schedules': schedules}
    return render(request, 'schedule.html', context)

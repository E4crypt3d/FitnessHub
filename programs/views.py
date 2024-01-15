from django.shortcuts import render
from .models import Exercise
# Create your views here.


def programs(request):
    exercises = Exercise.objects.all()
    context = {'exercises': exercises}
    return render(request, 'programs.html', context)

from django.contrib import admin
from .models import Schedule
from django.db import models
from django import forms
# Register your models here.


class AdminScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    form = AdminScheduleForm
    list_display = ['id', 'title', 'start_time',
                    'end_time', 'get_duration', 'timing', 'available']
    list_display_links = ['id', 'title', 'start_time',
                          'end_time', 'get_duration', 'timing', 'available']
    readonly_fields = ['available', 'title', 'duration', 'timing']

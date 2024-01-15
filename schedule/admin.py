from django.contrib import admin
from .models import Schedule
# Register your models here.


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_time',
                    'end_time', 'duration', 'timing', 'available']
    list_display_links = ['id', 'title', 'start_time',
                          'end_time', 'duration', 'timing', 'available']
    readonly_fields = ['available', 'title', 'duration', 'timing']

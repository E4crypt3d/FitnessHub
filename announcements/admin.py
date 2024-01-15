from django.contrib import admin
from .models import Announcement
# Register your models here.


@admin.register(Announcement)
class AdminAnnouncement(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'added_at',
                    'active', 'schedule', 'pricing', 'exercises']
    list_display_links = ['id', 'title', 'category',
                          'added_at', 'active', 'schedule', 'pricing', 'exercises']
    readonly_fields = ['schedule', 'pricing', 'exercises']

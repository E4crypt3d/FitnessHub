from django.contrib import admin
from .models import Exercise
# Register your models here.


@admin.register(Exercise)
class AdminExercise(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'added_at']
    list_display_links = ['id', 'title', 'body', 'added_at']

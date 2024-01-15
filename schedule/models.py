from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime, timedelta, time
from django.core.exceptions import ValidationError


class ScheduleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Schedule(models.Model):
    title = models.CharField(max_length=90)
    max_participants = models.PositiveIntegerField(default=25)
    current_participants = models.PositiveIntegerField(
        default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)
    timing = models.CharField(max_length=20)
    available = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()
    timings = ScheduleManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.title = f"{self.start_time.strftime(
                "%I:%M %p")} - {self.end_time.strftime("%I:%M %p")}"
            start_datetime = datetime.combine(
                datetime.today(), self.start_time)
            end_datetime = datetime.combine(datetime.today(), self.end_time)
            time_gap = end_datetime - start_datetime
            self.duration = timedelta(seconds=time_gap.seconds)
            Morning = time(12, 0)
            Afternoon = time(15, 0)
            if self.start_time < Morning:
                self.timing = 'Morning'
            elif self.start_time < Afternoon:
                self.timing = 'Afternoon'
            else:
                self.timing = 'Evening'
        if self.current_participants == self.max_participants:
            self.available = False
        if self.current_participants < self.max_participants:
            self.available = True
        return super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.current_participants > self.max_participants:
            raise ValidationError(
                "Current participants cannot exceed max participants.")

    @property
    def get_duration(self):
        duration = str(self.duration)
        split_duration = duration.split(':')
        for index, value in enumerate(split_duration):
            if int(value) == 00:
                continue
            else:
                if index == 0:
                    return f"{value} {'Hour' if int(value) == 1 else 'Hours'}"
                elif index == 1:
                    return f"{value} {'Minute' if int(value) == 1 else 'Minutes'}"

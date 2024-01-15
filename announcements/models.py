from django.db import models
from programs.models import Exercise
from schedule.models import Schedule
from pricing.models import Pricing
# Create your models here.


class ExerciseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category='Exercise, Specials and More', active=True)


class ScheduleUpdatesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category='Schedule Updates', active=True)


class DiscountDealsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category='DISCOUNTS, DEALS, and PROMOS!', active=True)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Announcement(models.Model):
    TYPES = [
        ('Exercise, Specials and More', 'Exercise, Specials and More'),
        ('Schedule Updates', 'Schedule Updates'),
        ('DISCOUNTS, DEALS, and PROMOS!', 'DISCOUNTS, DEALS, and PROMOS!'),
    ]
    category = models.CharField(max_length=38, choices=TYPES)
    title = models.CharField(max_length=90)
    body = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    schedule = models.OneToOneField(
        Schedule, related_name='announcement', on_delete=models.CASCADE, blank=True, null=True)
    pricing = models.OneToOneField(
        Pricing, related_name='announcement', on_delete=models.CASCADE, blank=True, null=True)
    exercises = models.OneToOneField(
        Exercise, related_name='announcement', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()
    workout = ExerciseManager()
    schedules = ScheduleUpdatesManager()
    ddp = DiscountDealsManager()
    actives = ActiveManager()

    def __str__(self):
        return self.title

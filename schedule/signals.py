from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Schedule
from announcements.models import Announcement


def handle_announcement_schedule(instance):
    templates = {
        'title': f'New Schedule Alert: {instance.title}',
        'body': f'''
            <h1>We are pleased to announce a new schedule: {instance.title}</h1>
            <ul>
            <li>- Time: {instance.start_time.strftime("%I:%M %p")} - {instance.end_time.strftime("%I:%M %p")}</li>
            <li>- Duration: {instance.get_duration}<li>
            </ul>
            <p>Your commitment to fitness is truly commendable, and we look forward to seeing you at this upcoming session.</p>
            <p> Best Regards,<p>
            <p> The FITNESS HUB Team</p>
                '''
    }
    return templates


@receiver(post_save, sender=Schedule)
def annouce_schedule(sender, instance, created, **kwargs):
    templates = handle_announcement_schedule(instance)
    if not created:
        announcement = instance.announcement
        announcement.title = templates['title']
        announcement.body = templates['body']
        if instance.available:
            announcement.active = True
        else:
            announcement.active = False
        announcement.save()
    else:
        cat = 'Schedule Updates'
        Announcement.objects.create(
            category=cat, title=templates['title'], body=templates['body'], active=True, schedule=instance)

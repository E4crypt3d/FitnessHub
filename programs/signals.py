from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Exercise
from announcements.models import Announcement


def handle_announcement_exercise(instance):
    templates = {
        'title': '🏋️‍♂️ Introducing New Exercise at FITNESS HUB!',
        'body': f'''
            <ul>
            <li>- 🌟 {instance.title}</li>
            <li>- 💪 {instance.body}<li>
            </ul>
            <p>🚀 Try it out during your next session and feel the burn! Stay tuned for more exciting updates on our ever-evolving fitness offerings.</p>
            <p> Let's crush those fitness goals together! 💪🔥<p>
            <p> The FITNESS HUB Team</p>

                '''
    }
    return templates


@receiver(post_save, sender=Exercise)
def annouce_exercise(sender, instance, created, **kwargs):
    templates = handle_announcement_exercise(instance)
    if not created:
        announcement = instance.announcement
        announcement.title = templates['title']
        announcement.body = templates['body']
        announcement.active = True
        announcement.save()
    else:
        cat = 'Exercise, Specials and More'
        Announcement.objects.create(
            category=cat, title=templates['title'], body=templates['body'], active=True, exercises=instance)

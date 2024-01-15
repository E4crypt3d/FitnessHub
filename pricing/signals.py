from django.dispatch import receiver
from .models import Pricing
from django.db.models.signals import post_save
from announcements.models import Announcement


@receiver(post_save, sender=Pricing)
def annouce_pricing(sender, instance, created, **kwargs):
    def handle_announcement_pricing(instance):
        if not instance.discount_price:
            templates = {
                'title': '🌟 Exciting News at FITNESS HUB!',
                'body': f'''
                <h1>New Pricing:</h1>
                <ul>
                <li>- Name: {instance.name}</li>
                <li>- Price: Rs.{instance.price}<li>
                <li>- Membership: {instance.membership_time}<li>
                </ul>
                <p>Your fitness journey starts here! 💪🏋️‍♀️</p>
                <p> The FITNESS HUB Team</p>

                    '''
            }
        else:
            templates = {
                'title': '🌟 Exciting News at FITNESS HUB!',
                'body': f'''
                <h1>New Pricing:</h1>
                <ul>
                <li>- Name: {instance.name}</li>
                <li>- Price: Rs.{instance.price} <span class="line-through"> Rs.{instance.discount_price}</span><li>
                <li>- Discount: {instance.discount_percentage()}%<li>
                <li>- Membership: {instance.membership_time}<li>
                </ul>
                <p>Your fitness journey starts here! 💪🏋️‍♀️</p>
                <p> The FITNESS HUB Team</p>

                    '''
            }
        return templates

    template = handle_announcement_pricing(instance)
    if not created and instance.announcement:
        announcement = instance.announcement
        announcement.title = template['title']
        announcement.body = template['body']
        announcement.active = True
        announcement.save()
    else:
        cat = 'DISCOUNTS, DEALS, and PROMOS!'
        Announcement.objects.create(
            category=cat, title=template['title'], body=template['body'], active=True, pricing=instance)

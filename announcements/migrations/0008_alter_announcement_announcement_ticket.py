# Generated by Django 4.2.7 on 2024-01-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0007_announcement_announcement_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement_ticket',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]

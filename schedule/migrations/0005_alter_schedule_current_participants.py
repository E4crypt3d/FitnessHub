# Generated by Django 4.2.7 on 2024-01-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_schedule_current_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='current_participants',
            field=models.PositiveIntegerField(default=0, max_length=models.PositiveIntegerField(default=25)),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_alter_schedule_current_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='current_participants',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

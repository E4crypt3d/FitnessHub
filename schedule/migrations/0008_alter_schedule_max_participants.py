# Generated by Django 4.2.7 on 2024-01-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_schedule_current_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='max_participants',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
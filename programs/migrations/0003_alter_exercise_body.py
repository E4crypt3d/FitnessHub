# Generated by Django 4.2.7 on 2024-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_alter_exercise_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(max_length=200, upload_to='excercise'),
        ),
    ]

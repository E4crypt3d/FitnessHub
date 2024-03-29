# Generated by Django 4.2.7 on 2023-12-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('body', models.TextField(max_length=280)),
                ('image', models.ImageField(max_length=200, upload_to='media/excercise')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

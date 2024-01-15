# Generated by Django 4.2.7 on 2023-12-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Specials', 'Specials'), ('Schedule Updates & More!', 'Schedule Updates & More!'), ('DISCOUNTS, DEALS, and PROMOS!', 'DISCOUNTS, DEALS, and PROMOS!')], max_length=38)),
                ('title', models.CharField(max_length=90)),
                ('body', models.TextField(max_length=244)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
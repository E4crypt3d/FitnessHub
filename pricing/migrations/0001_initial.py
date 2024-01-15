# Generated by Django 4.2.7 on 2023-12-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=0)),
                ('details', models.CharField(max_length=144)),
                ('membership_time', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')], max_length=12)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
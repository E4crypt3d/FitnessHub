# Generated by Django 4.2.7 on 2024-01-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0003_pricing_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='details',
            field=models.TextField(max_length=1000),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-03 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_bookingdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdb',
            name='City',
        ),
    ]

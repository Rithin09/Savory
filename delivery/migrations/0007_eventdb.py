# Generated by Django 4.2.5 on 2023-11-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_bookingdb_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eventname', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='Eventimage')),
            ],
        ),
    ]

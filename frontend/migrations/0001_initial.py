# Generated by Django 4.2.5 on 2023-10-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=70, null=True)),
                ('Email', models.CharField(blank=True, max_length=70, null=True)),
                ('Message', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=70, null=True)),
                ('Email', models.CharField(blank=True, max_length=70, null=True)),
                ('Password', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]

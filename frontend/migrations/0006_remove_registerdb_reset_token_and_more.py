# Generated by Django 4.2.5 on 2023-11-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_registerdb_reset_token_registerdb_token_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdb',
            name='reset_token',
        ),
        migrations.RemoveField(
            model_name='registerdb',
            name='token_expiration',
        ),
        migrations.AlterField(
            model_name='registerdb',
            name='Email',
            field=models.CharField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]

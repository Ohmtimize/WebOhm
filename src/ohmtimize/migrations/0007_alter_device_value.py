# Generated by Django 4.2.13 on 2024-06-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohmtimize', '0006_device_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='value',
            field=models.FloatField(default=0, help_text='Enter device value'),
        ),
    ]

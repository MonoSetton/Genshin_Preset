# Generated by Django 4.1 on 2022-08-06 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presets', '0002_preset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='set',
        ),
    ]

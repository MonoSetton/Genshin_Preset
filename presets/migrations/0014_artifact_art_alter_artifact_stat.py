# Generated by Django 4.1 on 2022-08-07 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presets', '0013_artifact_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='art',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='art', to='presets.preset'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='stat',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

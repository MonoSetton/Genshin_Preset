# Generated by Django 4.1 on 2022-08-07 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updatedb', '0004_remove_character_image_alter_bow_ability_and_more'),
        ('presets', '0008_artifact_first_artifact_fourth_artifact_main_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='presets.preset'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updatedb.artifact_set'),
        ),
        migrations.AlterField(
            model_name='preset',
            name='name',
            field=models.CharField(max_length=65),
        ),
    ]

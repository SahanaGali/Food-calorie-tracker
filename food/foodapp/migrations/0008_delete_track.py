# Generated by Django 5.0 on 2024-02-04 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_rename_carb_track_ca_rename_fats_track_fa_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='track',
        ),
    ]

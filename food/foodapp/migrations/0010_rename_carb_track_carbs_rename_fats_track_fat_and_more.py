# Generated by Django 5.0 on 2024-02-04 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='carb',
            new_name='carbs',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='fats',
            new_name='fat',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='imgs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='names',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='proteins',
            new_name='protein',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='quantitys',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='vitamin',
            new_name='vitamins',
        ),
    ]
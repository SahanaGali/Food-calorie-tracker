# Generated by Django 5.0 on 2024-01-31 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_remove_food_nutrients'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='img',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]

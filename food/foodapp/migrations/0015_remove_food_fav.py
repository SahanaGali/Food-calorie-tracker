# Generated by Django 5.0 on 2024-02-21 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0014_remove_food_favourite_food_fav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='fav',
        ),
    ]
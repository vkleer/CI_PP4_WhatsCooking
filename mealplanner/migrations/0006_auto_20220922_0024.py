# Generated by Django 3.2.15 on 2022-09-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0005_rename_mealoptiontomealplan_mealtomealplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealplan',
            old_name='meal_options',
            new_name='meal',
        ),
        migrations.RenameField(
            model_name='mealtomealplan',
            old_name='meal_option',
            new_name='meal',
        ),
    ]
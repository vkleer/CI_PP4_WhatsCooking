# Generated by Django 3.2.15 on 2022-09-22 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
        ('mealplanner', '0004_auto_20220921_2353'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MealOptionToMealPlan',
            new_name='MealToMealPlan',
        ),
    ]

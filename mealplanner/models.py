from django.db import models
from django.contrib.auth.models import User
from meal.models import Meal


class MealPlanner(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meal_planner',
    )
    meal_plans = models.ManyToManyField(
        'MealPlan', blank=True
    )

    def __str__(self):
        return self.user.username


class MealOption(models.Model):
    meal_plan = models.ForeignKey(
        'MealPlan', on_delete=models.CASCADE,
        related_name='meal_plan',
        default=''
    )
    meal_name = models.ForeignKey(
        Meal, on_delete=models.CASCADE,
        related_name='meal_name'
    )

    def __str__(self):
        return self.meal_name


class MealPlan(models.Model):
    # date should take the date that has been picked on the view_meal_planner
    # pageso that whenever the user clicks on a certain date, the correct
    # associated MealPlan is fetched
    meal_planner = models.ForeignKey(
        'MealPlanner', on_delete=models.CASCADE,
        related_name='meal_planner',
        default=''
    )
    date = models.CharField(max_length=25, unique=True)
    meal_options = models.ManyToManyField(
        MealOption, blank=True,
        )

    def __str__(self):
        return 'Meal plan ' + self.date + ' for ' + self.meal_planner.user.username

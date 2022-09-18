from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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


@receiver(post_save, sender=User)
def create_mealplanner(sender, instance=None, created=False, **kwargs):
    if created:
        MealPlanner.objects.create(user=instance,)


class MealOption(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE,
        related_name='meal',
    )

    def __str__(self):
        return self.meal.name


class MealOptionToMealPlan(models.Model):
    meal_option = models.ForeignKey('MealOption', on_delete=models.CASCADE)
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.CASCADE)


class MealPlan(models.Model):
    # date should take the date that has been picked on the view_meal_planner
    # pageso that whenever the user clicks on a certain date, the correct
    # associated MealPlan is fetched
    meal_planner = models.ForeignKey(
        'MealPlanner', on_delete=models.CASCADE,
        related_name='meal_planner',
    )
    date = models.CharField(max_length=25, unique=True)
    meal_options = models.ManyToManyField(
        MealOption,
        through='MealOptionToMealPlan'
        )

    def __str__(self):
        return 'Meal plan ' + self.date + ' for ' + self.meal_planner.user.username

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from meal.models import Meal
from datetime import datetime, timedelta


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
    date = models.DateField()
    meal_options = models.ManyToManyField(
        MealOption,
        through='MealOptionToMealPlan'
        )

    def __str__(self):
        return 'Meal plan ' + datetime.strptime(format(self.date), '%Y-%M-%d').strftime('%d/%M/%Y') + ' for ' + self.meal_planner.user.username


class Calendar(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='calendar',
    )
    picked_date = models.DateTimeField(default=datetime.now, blank=True)
    day_one = models.DateField(blank=True, null=True)
    day_two = models.DateField(blank=True, null=True)
    day_three = models.DateField(blank=True, null=True)
    day_four = models.DateField(blank=True, null=True)
    day_five = models.DateField(blank=True, null=True)
    day_six = models.DateField(blank=True, null=True)
    day_seven = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Calendar for ' + self.user.username

    def clean(self):
        self.day_one = self.picked_date
        self.day_two = self.day_one + timedelta(days=1)
        self.day_three = self.day_one + timedelta(days=2)
        self.day_four = self.day_one + timedelta(days=3)
        self.day_five = self.day_one + timedelta(days=4)
        self.day_six = self.day_one + timedelta(days=5)
        self.day_seven = self.day_one + timedelta(days=6)

    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)


@receiver(post_save, sender=User)
def create_models(sender, instance=None, created=False, **kwargs):
    if created:
        MealPlanner.objects.create(user=instance,)
        Calendar.objects.create(user=instance,)

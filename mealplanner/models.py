from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from meal.models import Meal
from datetime import datetime, timedelta


class MealPlanner(models.Model):
    """
    A class for the MealPlanner model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meal_planner',
    )
    meal_plans = models.ManyToManyField(
        'MealPlan', blank=True
    )

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.user.username


class MealToMealPlan(models.Model):
    """
    A class for the MealToMealPlan model
    """
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, blank=True, null=True
    )
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return (
            '(' + str(self.id) + ') ' + str(self.meal) + ' to meal plan ' +
            datetime.strptime(
                format(self.meal_plan.date), '%Y-%M-%d'
            ).strftime('%d/%M/%Y')
        )


class MealPlan(models.Model):
    """
    A class for the MealPlan model
    """
    meal_planner = models.ForeignKey(
        'MealPlanner', on_delete=models.CASCADE,
        related_name='meal_planner',
    )
    date = models.DateField()
    meal = models.ManyToManyField(
        Meal,
        through='MealToMealPlan',
        blank=True
        )

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return (
            'Meal plan ' + datetime.strptime(
                format(self.date), '%Y-%M-%d'
            ).strftime('%d/%M/%Y') + ' for ' + self.meal_planner.user.username
        )


class Calendar(models.Model):
    """
    A class for the Calendar model
    """
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
        """
        Returns a more readable name for each object
        """
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
    """
    Creates a new MealPlanner and Calendar object on user creation
    """
    if created:
        MealPlanner.objects.create(user=instance,)
        Calendar.objects.create(user=instance,)

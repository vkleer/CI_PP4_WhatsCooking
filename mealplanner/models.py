from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from meal.models import Meal


class MealPlanner(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meal_planner'
    )

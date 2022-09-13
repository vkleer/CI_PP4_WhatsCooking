from django.db import models
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient


class MealType(models.Model):
    type = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.type


class Diet(models.Model):
    diet = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.diet


class PrepTime(models.Model):
    prep_time = models.CharField(max_length=25)

    def __str__(self):
        return self.prep_time


class CookTime(models.Model):
    cook_time = models.CharField(max_length=25)

    def __str__(self):
        return self.cook_time


class Meal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = CloudinaryField(
        'image', default='placeholder'
    )
    description = models.TextField()
    ingredients = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        MealType, on_delete=models.CASCADE
    )
    diet = models.ForeignKey(
        Diet, on_delete=models.CASCADE
    )
    prep_time = models.ForeignKey(
        PrepTime, on_delete=models.CASCADE
    )
    cook_time = models.ForeignKey(
        CookTime, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

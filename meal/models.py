from django.db import models
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    """
    A class for the Ingredient model
    """
    ingredient = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.ingredient


class IngredientToRecipe(models.Model):
    """
    A class for the IngredientToRecipe model
    """
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)


class MealType(models.Model):
    """
    A class for the MealType model
    """
    type = models.CharField(max_length=25, unique=True)

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.type


class Diet(models.Model):
    """
    A class for the Diet model
    """
    diet = models.CharField(
        max_length=25, blank=True, null=True, unique=True,
        default=''
        )

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.diet


class PrepTime(models.Model):
    """
    A class for the PrepTIme model
    """
    prep_time = models.CharField(max_length=25)

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.prep_time


class CookTime(models.Model):
    """
    A class for the CookTime model
    """
    cook_time = models.CharField(max_length=25)

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.cook_time


class Meal(models.Model):
    """
    A class for the Meal model
    """
    name = models.CharField(max_length=200, unique=True)
    image = CloudinaryField(
        'image', default='placeholder'
    )
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientToRecipe'
        )
    type = models.ForeignKey(
        MealType, on_delete=models.CASCADE
    )
    diet = models.ForeignKey(
        Diet, blank=True, null=True,
        on_delete=models.CASCADE
    )
    prep_time = models.ForeignKey(
        PrepTime, on_delete=models.CASCADE
    )
    cook_time = models.ForeignKey(
        CookTime, on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Returns a more readable name for each object
        """
        return self.name

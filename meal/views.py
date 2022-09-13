from django.shortcuts import render
from django.views import generic, View
from .models import Meal, IngredientToRecipe


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('name')
    template_name = 'meals.html'
    paginate_by = 8


class MealDetail(View):
    def get(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        recipe_ingredients = IngredientToRecipe.objects.all()
        return render(request, 'meal_detail.html',
                      {'meal': meal,
                       'recipe_ingredients': recipe_ingredients})

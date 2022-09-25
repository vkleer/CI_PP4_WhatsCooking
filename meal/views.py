from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Meal, IngredientToRecipe


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('name')
    template_name = 'recipe_list.html'


@method_decorator(login_required, name='dispatch')
class MealDetail(View):
    def get(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        recipe_ingredients = IngredientToRecipe.objects.all()
        return render(request, 'recipe.html',
                      {'meal': meal,
                       'recipe_ingredients': recipe_ingredients})

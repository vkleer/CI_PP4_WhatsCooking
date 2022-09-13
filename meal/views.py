from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meal


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('name')
    template_name = 'meals.html'
    paginate_by = 8


class MealDetail(View):
    def get(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        return render(request, 'meal_detail.html',
                      {'meal': meal})

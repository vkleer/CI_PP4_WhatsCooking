from django.shortcuts import render
from django.views import generic
from meal.models import Meal


class MealPlanner(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('name')
    template_name = 'meal_planner.html'

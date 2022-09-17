from django.shortcuts import render
from django.views import generic
from .models import MealOption


class MealPlannerView(generic.ListView):
    model = MealOption
    queryset = MealOption.objects.all()
    template_name = 'meal_planner.html'

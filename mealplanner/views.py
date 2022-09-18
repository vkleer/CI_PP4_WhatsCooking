from django.shortcuts import render
from django.views import generic
from .models import MealOption, MealPlan


class MealPlannerView(generic.ListView):
    model = MealPlan
    queryset = MealPlan.objects.all()
    template_name = 'meal_planner.html'

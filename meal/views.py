from django.shortcuts import render
from django.views import generic
from.models import Meal


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('name')
    template_name = 'meals.html'
    paginate_by = 8

from django.shortcuts import render


def MealPlanner(request):
    return render(request, 'meal_planner.html')

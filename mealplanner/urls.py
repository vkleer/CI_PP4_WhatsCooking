from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealPlanner, name='meal_planner'),
]

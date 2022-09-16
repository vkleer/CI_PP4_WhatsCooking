from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealPlanner.as_view(), name='meal_planner'),
]

from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealPlannerView.as_view(), name='meal_planner'),
]

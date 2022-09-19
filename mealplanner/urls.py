from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealPlannerView.as_view(), name='meal_planner'),
    path('edit_meal_plan/<int:meal_plan_id>', views.EditMealPlan.as_view(), name='edit_meal_plan'),
]

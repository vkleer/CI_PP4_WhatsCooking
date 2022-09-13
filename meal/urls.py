from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealList.as_view(), name='meals'),
    path('meal_detail/<meal_id>', 
         views.MealDetail.as_view(), name='meal_detail')
]

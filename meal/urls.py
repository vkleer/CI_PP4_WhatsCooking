from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealList.as_view(), name='recipe_list'),
    path('recipe/<meal_id>',
         views.MealDetail.as_view(), name='recipe')
]

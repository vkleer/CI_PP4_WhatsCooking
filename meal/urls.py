from . import views
from django.urls import path


urlpatterns = [
    path('', views.MealList.as_view(), name='meals')
]

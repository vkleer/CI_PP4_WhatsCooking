from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('profile/<str:pk>/', views.UserProfile, name="profile"),
]

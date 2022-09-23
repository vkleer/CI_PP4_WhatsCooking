from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('profile/<str:pk>/', views.UserProfile, name="profile"),
    path('delete_user/<str:pk>', views.DeleteUser, name='delete_user'),
    path('contact/', views.Contact, name='contact'),
]

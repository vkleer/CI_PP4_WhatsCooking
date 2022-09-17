from django.contrib import admin
from .models import MealPlanner, MealOption, MealPlan


admin.site.register(MealPlanner)
admin.site.register(MealOption)
admin.site.register(MealPlan)

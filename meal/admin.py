from django.contrib import admin
from .models import Meal, Ingredient, MealType, Diet, PrepTime, CookTime


admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(MealType)
admin.site.register(Diet)
admin.site.register(PrepTime)
admin.site.register(CookTime)

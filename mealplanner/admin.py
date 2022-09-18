from django.contrib import admin
from .models import MealPlanner, MealOption, MealPlan, MealOptionToMealPlan


class MealOptionToMealPlanInline(admin.TabularInline):
    model = MealOptionToMealPlan
    extra = 1


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    inlines = (MealOptionToMealPlanInline,)


admin.site.register(MealPlanner)
admin.site.register(MealOption)
admin.site.register(MealOptionToMealPlan)

from django.contrib import admin
from .models import *


class MealToMealPlanInline(admin.TabularInline):
    """
    An admin TabularInline class for the MealToMealPlanInline model
    """
    model = MealToMealPlan
    extra = 1


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    """
    An admin class for the MealPlanAdmin model
    """
    inlines = (MealToMealPlanInline,)


admin.site.register(MealPlanner)
admin.site.register(MealToMealPlan)
admin.site.register(Calendar)

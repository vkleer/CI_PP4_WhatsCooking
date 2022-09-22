from django.contrib import admin
from .models import *


class MealToMealPlanInline(admin.TabularInline):
    model = MealToMealPlan
    extra = 1


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    inlines = (MealToMealPlanInline,)


admin.site.register(MealPlanner)
admin.site.register(MealToMealPlan)
admin.site.register(Calendar)

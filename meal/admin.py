from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Meal, Ingredient, IngredientToRecipe, MealType, Diet, PrepTime, CookTime
)


class IngredientToRecipeInline(admin.TabularInline):
    """
    An admin TabularInline class for the IngredientToRecipeInline model
    """
    model = IngredientToRecipe
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    """
    An admin class for the IngredientAdmin model
    """
    inlines = (IngredientToRecipeInline,)


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    """
    An admin class for the MealAdmin model
    """
    summernote_fields = ('description')
    search_fields = ['name']
    inlines = (IngredientToRecipeInline,)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientToRecipe)
admin.site.register(MealType)
admin.site.register(Diet)
admin.site.register(PrepTime)
admin.site.register(CookTime)

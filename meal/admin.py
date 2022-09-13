from django.contrib import admin
from .models import Meal, Ingredient, IngredientToRecipe, MealType, Diet, PrepTime, CookTime
from django_summernote.admin import SummernoteModelAdmin


class IngredientToRecipeInline(admin.TabularInline):
    model = IngredientToRecipe
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (IngredientToRecipeInline,)


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    search_fields = ['name']
    inlines = (IngredientToRecipeInline,)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientToRecipe)
admin.site.register(MealType)
admin.site.register(Diet)
admin.site.register(PrepTime)
admin.site.register(CookTime)


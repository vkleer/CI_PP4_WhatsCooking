from django.contrib import admin
from .models import Meal, Ingredient, MealType, Diet, PrepTime, CookTime
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Meal)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    search_fields = ['name']


admin.site.register(Ingredient)
admin.site.register(MealType)
admin.site.register(Diet)
admin.site.register(PrepTime)
admin.site.register(CookTime)

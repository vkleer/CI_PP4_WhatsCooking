from django import forms
from .models import Calendar, MealPlan

class DateInput(forms.DateInput):
    input_type = 'date'

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('picked_date',)
        widgets = {
            'picked_date': DateInput()
        }

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['meal_options']

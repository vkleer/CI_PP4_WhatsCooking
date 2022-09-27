from django import forms
from .models import Calendar, MealPlan


class DateInput(forms.DateInput):
    """
    A class for the DateInput field
    """
    input_type = 'date'


class CalendarForm(forms.ModelForm):
    """
    A class for the Calendar form
    """
    class Meta:
        model = Calendar
        fields = ('picked_date',)
        widgets = {
            'picked_date': DateInput()
        }


class MealPlanForm(forms.ModelForm):
    """
    A class for the MealPlan form
    """
    class Meta:
        model = MealPlan
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True

from django.shortcuts import render, redirect
from django.views import generic
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
from .models import MealPlan, Calendar
from .forms import CalendarForm


class MealPlannerView(generic.View):
    def get(self, request):
        today = datetime.today()
        context = {
            'mealplan_list': MealPlan.objects.all(),
            'today': today,
            'calendar_form': CalendarForm(),
        }
        return render(request, 'meal_planner.html', context)

    def post(self, request):
        calendar = Calendar.objects.get(user=request.user)
        calendar_form = CalendarForm(request.POST, instance=calendar)

        if calendar_form.is_valid():
            try:
                calendar_form.save()
                return redirect('meal_planner')
            except IntegrityError as e:
                messages.error(request, 'You already have a plan available on this day.')

        else:
            messages.error(request, 'Something went wrong.')

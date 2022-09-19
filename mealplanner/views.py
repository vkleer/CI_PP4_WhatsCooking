from django.shortcuts import render, redirect, reverse
from django.views import generic
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
from .models import MealPlan, Calendar
from .forms import CalendarForm


class MealPlannerView(generic.View):
    def get(self, request):
        today = datetime.today()
        calendar = Calendar.objects.get(user=request.user)
        week = [
            calendar.day_one,
            calendar.day_two,
            calendar.day_three,
            calendar.day_four,
            calendar.day_five,
            calendar.day_six,
            calendar.day_seven,
        ]
        context = {
            'mealplan_list': MealPlan.objects.all(),
            'today': today,
            'calendar_form': CalendarForm(initial={'picked_date': calendar.picked_date}),
            'user_calendar': calendar,
            'week': week,
        }
        return render(request, 'meal_planner.html', context)

    def post(self, request):
        calendar = Calendar.objects.get(user=request.user)
        calendar_form = CalendarForm(request.POST, instance=calendar)

        if calendar_form.is_valid():
            try:
                calendar_form.save()
                return redirect(reverse('meal_planner'))
            except IntegrityError as e:
                messages.error(request, 'You already have a plan available on this day.')

        else:
            messages.error(request, 'Something went wrong.')

from django import forms
from django.shortcuts import render, redirect, reverse
from django.views import generic
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
# from django.forms import formset_factory
from django.forms import inlineformset_factory
from .models import MealPlan, MealOptionToMealPlan, Calendar
from .forms import CalendarForm, MealPlanForm


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


class EditMealPlan(generic.View):
    def get(self, request, meal_plan_id):
        MealOptionFormSet = inlineformset_factory(MealPlan, MealOptionToMealPlan, fields=('meal_option',), extra=9, max_num=10)
        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        formset = MealOptionFormSet(instance=meal_plan)
        context = {
            'meal_plan': meal_plan,
            'formset': formset,
        }
        return render(request, 'edit_meal_plan.html', context)

    def post(self, request, meal_plan_id):
        MealOptionFormSet = inlineformset_factory(MealPlan, MealOptionToMealPlan, fields=('meal_option',), extra=9, max_num=10)
        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        formset = MealOptionFormSet(request.POST, instance=meal_plan)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('meal_planner'))

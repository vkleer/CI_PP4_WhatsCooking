from django.shortcuts import render, redirect, reverse
from django.views import generic
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import MealPlan, MealPlanner, MealToMealPlan, Calendar
from .forms import CalendarForm, MealPlanForm


class MealPlannerView(generic.View):
    """
    A view class to display the meal planner
    """
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
            'calendar_form': CalendarForm(
                initial={'picked_date': datetime.today().strftime('%Y-%m-%d')}
            ),
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
                messages.error(
                    request, 'You already have a plan available on this day.'
                )

        else:
            messages.error(request, 'Something went wrong.')


class CreateMealPlan(generic.View):
    """
    A view class to display the meal plan creation page
    """
    def get(self, request, meal_plan_date):
        MealOptionFormSet = inlineformset_factory(
            MealPlan, MealToMealPlan, fields=('meal',), extra=10, max_num=10
        )
        form = MealPlanForm(initial={
            'date': meal_plan_date,
        })
        formset = MealOptionFormSet()
        context = {
            'form': form,
            'formset': formset,
        }
        return render(request, 'create_meal_plan.html', context)

    def post(self, request, meal_plan_date):
        MealOptionFormSet = inlineformset_factory(
            MealPlan, MealToMealPlan, fields=('meal',), extra=10, max_num=10
        )
        form = MealPlanForm(request.POST)
        if form.is_valid():
            meal_planner = MealPlanner.objects.get(user=request.user)
            date = form.cleaned_data.get('date')
            meal_plan = MealPlan(meal_planner=meal_planner, date=date)
            meal_plan.save()
            formset = MealOptionFormSet(request.POST, instance=meal_plan)
        else:
            messages.warning(request, "Form could not be validated - meal plan won't be created.")
            return redirect(reverse('meal_planner'))
        if formset.is_valid():
            formset.save()
            messages.success(request, "Successfully created new meal plan.")
            return redirect(reverse('meal_planner'))
        else:
            messages.warning(request, "Formset could not be validated - meal plan won't be created.")
            return redirect(reverse('meal_planner'))


class EditMealPlan(generic.View):
    """
    A view class to display the meal plan edit page
    """
    def get(self, request, meal_plan_id):
        MealOptionFormSet = inlineformset_factory(
            MealPlan, MealToMealPlan, fields=('meal',), extra=9, max_num=10
        )
        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        formset = MealOptionFormSet(instance=meal_plan)
        context = {
            'meal_plan': meal_plan,
            'formset': formset,
        }
        return render(request, 'edit_meal_plan.html', context)

    def post(self, request, meal_plan_id):
        MealOptionFormSet = inlineformset_factory(
            MealPlan, MealToMealPlan, fields=('meal',), extra=9, max_num=10
        )
        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        formset = MealOptionFormSet(request.POST, instance=meal_plan)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Meal plan updated succesfully.')
            return redirect(reverse('meal_planner'))


class DeleteMealPlan(generic.View):
    """
    A view class to display the meal plan deletion modal
    """
    def post(self, request, meal_plan_id):
        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        meal_plan.delete()
        messages.success(
            request,
            'Meal plan deleted succesfully.'
        )
        return redirect(reverse('meal_planner'))

function getCalendarCells() {
    calendar = document.getElementById('meal-planner-calendar')
    cells = calendar.children

    for (i = 0; i < cells.length; i++) {
        mealPlanButton = cells[i].querySelector('.btn');
        mealPlanId = cells[i].querySelector('input[name=meal_plan_id]')
        if (cells[i].children.length > 3 ) {
            cells[i].style.cssText = 'vertical-align:top';
            mealPlanButton.innerHTML = 'Edit plan';
            mealPlanButton.href = `edit_meal_plan/${mealPlanId.value}`;
        }
        else {
            mealPlanDate = cells[i].querySelector('input[name=meal_plan_date]')
            mealPlanButton.href = `create_meal_plan/${mealPlanDate.value}`;
            cells[i].style.cssText = 'vertical-align:center';
            mealPlanButton.innerHTML = 'Create plan';
        }
    }
}

function hideFormSelect() {
    mealPlannerSel = document.getElementById('id_meal_planner')
    dateSel = document.getElementById('id_date')

    mealPlannerSel.setAttribute('hidden', '')
    dateSel.setAttribute('hidden', '')
}
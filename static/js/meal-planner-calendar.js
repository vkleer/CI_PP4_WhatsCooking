function getCalendarCells() {
    calendar = document.getElementById('meal-planner-calendar')
    cells = calendar.children

    for (i = 0; i < cells.length; i++) {
        mealPlanButton = cells[i].querySelector('.btn');
        mealPlanId = cells[i].querySelector('input[name=meal_plan_id]')
        console.log(mealPlanId)
        if (cells[i].children.length > 2 ) {
            cells[i].style.cssText = 'vertical-align:top';
            mealPlanButton.innerHTML = 'Edit plan';
            mealPlanButton.href = `edit_meal_plan/${mealPlanId.value}`;
        }
        else {
            mealPlanButton.href = '/';
            cells[i].style.cssText = 'vertical-align:center';
            mealPlanButton.innerHTML = 'Create plan';
        }
    }
}

getCalendarCells();
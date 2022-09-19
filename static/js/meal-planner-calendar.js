function getCalendarCells() {
    calendar = document.getElementById('meal-planner-calendar')
    cells = calendar.children

    for (i = 0; i < cells.length; i++) {
        if (cells[i].children.length > 1 ) {
            mealPlanButton = cells[i].querySelector('.btn');
            mealPlanButton.innerHTML='Edit meal plan';
            mealPlanButton.href='editView';
            console.log(mealPlanButton);
        }
    }
}

getCalendarCells();
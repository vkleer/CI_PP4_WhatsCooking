function setDelBtnToMealPlanId(currentButton) {
    mealPlanId = currentButton.parentNode.querySelector('input[name=meal_plan_id]').value
    modal = document.getElementById('deletion-form');
    modal.setAttribute('action', `delete_meal_plan/${mealPlanId}`);
}

function setCalDefDate() {
    datePick = document.querySelector('input[name=picked_date]');
    datePick.classList.add('form-control');
    calBtn = document.getElementById('cal-btn');
}

function getCalendarCells() {
    calendar = document.getElementById('meal-planner-calendar')
    cells = calendar.children

    for (i = 0; i < cells.length; i++) {
        mealPlanButton = cells[i].querySelector('.btn');
        mealPlanId = cells[i].querySelector('input[name=meal_plan_id]')
        if (cells[i].children.length > 3 ) {
            let deleteButton = document.createElement('button');
            deleteButton.classList.add('btn', 'btn-danger', 'btn-del');
            deleteButton.innerHTML = `<i class="far fa-trash-alt"></i>`;
            deleteButton.setAttribute('data-toggle', 'modal');
            deleteButton.setAttribute('data-target', '#deletionModal');
            mealPlanButton.parentNode.insertBefore(deleteButton, mealPlanButton.nextSibling);
            cells[i].style.cssText = 'vertical-align:top';
            mealPlanButton.innerHTML = `<i class="fas fa-pen"></i>`;
            mealPlanButton.href = `edit_meal_plan/${mealPlanId.value}`;
            deleteButton.addEventListener('click', function() {
                setDelBtnToMealPlanId(deleteButton);
            });
        }
        else {
            mealPlanDate = cells[i].querySelector('input[name=meal_plan_date]');
            mealPlanButton.classList.remove('btn-primary');
            mealPlanButton.classList.add('btn-success', 'btn-add');
            mealPlanButton.href = `create_meal_plan/${mealPlanDate.value}`;
            cells[i].style.cssText = 'vertical-align:center';
            mealPlanButton.innerHTML = `<i class="fas fa-plus"></i>`;
        }
    }
}

function hideFormSelect() {
    mealPlannerSel = document.getElementById('id_meal_planner')
    dateSel = document.getElementById('id_date')

    mealPlannerSel.setAttribute('hidden', '')
    dateSel.setAttribute('hidden', '')
}
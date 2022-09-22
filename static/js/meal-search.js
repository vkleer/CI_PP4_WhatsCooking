function filterDietType() {
    // Variables for diet type filter
    const dietTypeSelect = document.getElementById('diet-type-select');
    let dietTypeOption = dietTypeSelect.options[dietTypeSelect.selectedIndex].text;
    // Variables for meals
    const mealsList = document.getElementById('meals-list');
    let meal = mealsList.getElementsByClassName('meal-card');

    // Diet type filter
    for (i = 0; i < meal.length; i++) {
        let dietType = meal[i].getElementsByClassName('diet-type')[0];
        let dietTypeVal = dietType.textContent;
        if (dietTypeOption === 'Any') {
            meal[i].style.display = '';
            meal[i].classList.add('diet-filter-any');
            meal[i].classList.remove('diet-filter');   
        } else if (dietTypeVal === dietTypeOption) {
            meal[i].style.display = '';
            meal[i].classList.add('diet-filter');
            meal[i].classList.remove('diet-filter-any');
        } else {
            meal[i].style.display = 'none';
            meal[i].classList.remove('diet-filter');
            meal[i].classList.remove('diet-filter-any');
        }
    }
}

function searchMeals() {
    // Variables for search field
    const search = document.getElementById('meal-search');
    let filter = search.value.toUpperCase();
    // Variables for meals
    const mealsList = document.getElementById('meals-list');
    let meal = mealsList.getElementsByClassName('meal-card');

    for (i = 0; i < meal.length; i++) {
        let mealName = meal[i].getElementsByClassName('card-title')[0];
        let mealNameVal = mealName.textContent;
        if (mealNameVal.toUpperCase().indexOf(filter) > -1) {
            if (meal[i].classList.contains('diet-filter')) {
                meal[i].style.display = '';
                meal[i].classList.add('search-filter');
            } else if (meal[i].classList.contains('diet-filter-any')) {
                meal[i].style.display = '';
                meal[i].classList.add('search-filter');
            }
        } else {
            meal[i].style.display = 'none';
            meal[i].classList.remove('search-filter');
        }
    }
}

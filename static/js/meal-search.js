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

function toggleMealTypes() {
    // Variables for every meal type list div
    const breakfastList = document.getElementById('breakfast-list');
    const lunchList = document.getElementById('lunch-list');
    const dinnerList = document.getElementById('dinner-list');
    const snackList = document.getElementById('snack-list');
    const mealTypeLists = [breakfastList, lunchList, dinnerList, snackList];
    // Variables for every meal type checkbox
    const breakfastToggle = document.getElementById('breakfast-toggle');
    const lunchToggle = document.getElementById('lunch-toggle');
    const dinnerToggle = document.getElementById('dinner-toggle');
    const snackToggle = document.getElementById('snack-toggle');
    const mealTypeToggles = [breakfastToggle, lunchToggle, dinnerToggle, snackToggle];

    for (i = 0; i < mealTypeToggles.length; i++) {
        if (mealTypeToggles[i].checked) {
            mealTypeLists[i].style.display = '';
        } else {
            mealTypeLists[i].style.display = 'none';
        }
    }
}
function filterMeals() {
    // Variables for meat type filter
    let mealTypeSelect = document.getElementById('meal-type-select');
    let mealTypeOption = mealTypeSelect.options[mealTypeSelect.selectedIndex].text;
    // Variables for meals
    let mealsList = document.getElementById('meals-list');
    let meal = mealsList.getElementsByClassName('meal-card');

    // Meal type filter
    for (i = 0; i < meal.length; i++) {
        let mealType = meal[i].getElementsByClassName('meal-type')[0];
        let mealTypeVal = mealType.textContent || mealType.innerText;
        if (mealTypeOption === 'Any') {
            meal[i].style.display = '';
            meal[i].classList.remove('meat-filter');
            meal[i].classList.add('meat-filter-any');        }
        else if (mealTypeVal === mealTypeOption) {
            meal[i].style.display = '';
            meal[i].classList.add('meat-filter');
            meal[i].classList.remove('meat-filter-any');
        } else {
            meal[i].style.display = 'none';
            meal[i].classList.remove('meat-filter');
            meal[i].classList.remove('meat-filter-any');
        }
    }
}

function searchMeals() {
    // Variables for search field
    let search = document.getElementById('meal-search');
    let filter = search.value.toUpperCase();
    // Variables for meals
    let mealsList = document.getElementById('meals-list');
    let meal = mealsList.getElementsByClassName('meal-card');

    for (i = 0; i < meal.length; i++) {
        let mealName = meal[i].getElementsByClassName('card-title')[0];
        let mealNameVal = mealName.textContent || mealName.innerText;
        if (mealNameVal.toUpperCase().indexOf(filter) > -1) {
            if (meal[i].classList.contains('meat-filter')) {
                meal[i].style.display = '';
                meal[i].classList.add('search-filter');
            } else if (meal[i].classList.contains('meat-filter-any')) {
                meal[i].style.display = '';
                meal[i].classList.add('search-filter');
            }
        } else {
            meal[i].style.display = 'none';
            meal[i].classList.remove('search-filter');
        }
    }
}

// function filterMeals() {
//     // Variables for meat type filter
//     let mealTypeSelect = document.getElementById('meal-type-select');
//     let mealTypeOption = mealTypeSelect.options[mealTypeSelect.selectedIndex].text;
//     // Variables for diet type filter
//     // let dietTypeSelect = document.getElementById('diet-type-select');
//     // let dietTypeOption = dietTypeSelect.options[dietTypeSelect.selectedIndex].text;
//     // Variables for meals
//     let mealsList = document.getElementById('meals-list');
//     let meal = mealsList.getElementsByClassName('meal-card');

//     // Meal type filter
//     for (i = 0; i < meal.length; i++) {
//         let mealType = meal[i].getElementsByClassName('meal-type')[0];
//         let mealTypeVal = mealType.textContent || mealType.innerText;
//         // let dietType = meal[i].getElementsByClassName('diet-type')[0];
//         // let dietTypeVal = dietType.textContent || dietType.innerText;
//         if (mealTypeOption === 'Any') {
//             meal[i].style.display = '';
//         }
//         else if (mealTypeVal === mealTypeOption) {
//             meal[i].style.display = '';
//         } else {
//             meal[i].style.display = "none";
//         }
//     }
// }
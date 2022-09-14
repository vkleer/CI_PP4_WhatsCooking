let input = document.getElementById('meal-search');
let filter = input.value.toUpperCase();
let mealsList = document.getElementById('meals-list');
let meal = mealsList.getElementsByClassName('meal-card');

function searchMeals() {
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < meal.length; i++) {
        let meal = meal;
        let cards = meal[i].getElementsByClassName('card-title')[0];
        let txtValue = cards.textContent || cards.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            meal[i].style.display = "";
        } else {
            meal[i].style.display = "none";
        }
    }
}

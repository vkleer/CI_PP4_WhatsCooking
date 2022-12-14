# What's Cooking?
(Developer: Vilayat Kleer)

![mockup-image.jpg](docs/mockup-image.jpg)

[View the live website](https://ci-pp4-whatscooking.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Application Owner Goals](#application-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
3. [User Stories](#user-stories)
    1. [User](#user)
    1. [Returning User](#returning-user)
    3. [Application Owner](#application-owner)
4. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Structure](#structure)
5. [Technical Design](#technical-design)
    1. [Database](#database)
        1. [Database Models](#database-models)
6. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Framework](#framework)
    3. [Tools & Libraries](#tools--libraries)
7. [Features](#features)
8. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [Css Validation](#css-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Python Validation](#python-validation)
    5. [Accessibility Wave WebAIM](#accessibility-wave-webaim)
    6. [Performance Google Lighthouse](#performance-google-lighthouse)
9. [Testing](#validation)
    1. [Manual Testing - User Stories](#manual-testing---user-stories)
    2. [Automated Testing](#automated-testing)
10. [Bugs](#Bugs)
11. [Deployment](#deployment)
    1. [GitHub](#github)
    2. [Heroku](#heroku)
    3. [Google SMTP Server](#google-smtp-server)
12. [Credits](#credits)
    1. [Images](#images)
    2. [Code](#code)
13. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
- Be able to create meal plans to become a better meal-prepper
- Be able to edit or delete my meal plans at any given time
- Have an overview of all my meal plans for a set week
- Get inspired by finding new recipes

### Application Owner Goals
- Create an application that helps users track and prep their meals
- Provide users with a database full of recipes for them to choose and get inspired by
- Provide feedback to users on any important action (CRUD, log in, log out etc.)
- Deliver an aesthetically pleasing design to the application that makes users want to come back

## User Experience

### Target Audience
- People who want to keep track of their daily meals
- Meal preppers who want an organised space for their meal plans
- Cooking enthusiasts who want to get inspired by new recipes without looking on multiple websites

### User Requirements and Expectations
- A simple, elegant application that anyone can use
- Clear feedback provided after performing an important action
- Providing a personal touch by referring to the users' username and first name throughout the application

## User Stories

### Anonymous User
1. As an anonymous user, I want to be able to view the home page, so I know what the application is about
2. As an anonymous user, I want to be able to view the recipe list, so I get a taste of what the application has to offer
3. As an anonymous user, I want to be able to create an account, so I can start using the application

### Registered User
4. As a registered user, I want to be able to log in with my account
5. As a registered user, I want to be able to create a meal plan for a specific date
6. As a registered user, I want to be able to add meals to a meal plan
7. As a registered user, I want to be able to edit any of my meal plans
8. As a registered user, I want to be able to delete any of my meal plans
9. As a registered user, I want to have a weekly overview of my meal plans in my meal planner
10. As a registered user, I want to be able to pick the first day of the week of my weekly overview
11. As an registered user, I want to be able to view the recipe list
12. As a registered user, I want to be able to view the details of each recipe in the recipe list
13. As a registered user, I want to be able to view my account details on my profile page
14. As a registered user, I want to be able to delete my account on my profile page
15. As a registered user, I want to be able to log out when I'm done
16. As a registered user, I want to receive feedback after performing an important action

### Application Owner
17. As the application owner, I want users to be able to filter recipes by meal type, diet type or by using the search bar
18. As the application owner, I want to restrict most of the applications' functionality for anonymous users to encourage them to create an account
19. As the application owner, I want users to stay on the application when they receive an HTTP response of 400, 403, 404 or 500
20. As the application owner, I want users to be able to contact me with a contact form
21. As the application owner, I want users to be able to find me on GitHub
22. As the application owner, I want the users' input on forms to be validated
23. As the application owner, I want users to be able to navigate around the application easily
24. As the application owner, I want to provide a responsive application for all devices

## Design

### Colours
The colours I used for the application have been picked using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel). I first found a 'main' colour that I wanted to use (#407464, used in the bg-main class) before moving on to the other colours. The 'Split Complementary' colour harmony rule suggested a dark pink colour, which I took and customized to a soft grey-pink colour (#f5e4e4, used in the bg-accent class) to make it easier to look at and use in the application. Finally, I simply took the main colour and made it a few shades darker to use for the navbar and footer (#2e4b42, used in the bg-main-dark class).

<details><summary>Screenshot of Adobe Color Wheel</summary>
    <img src="docs/design/adobe-color-wheel.JPG">
</details>

### Fonts
The fonts that I used are [Reem Kufi Fun](https://fonts.google.com/specimen/Reem+Kufi+Fun) for the logo, [Montserrat](https://fonts.google.com/specimen/Montserrat) for all the headings and [Quicksand](https://fonts.google.com/specimen/Quicksand) for all other text elements. They are all sans-serif fonts, but have a few distinct differences: The Montserrat font creates a nice contrast with the other text elements by having a simple design and bold font-weight, while the Quicksand font is more playful, yet legible. The Reem Kufi Fun font stands out from the other fonts with its unique 'W', which is why I found it to be suitable for the logo. All fonts have sans-serif as a fallback.

### Structure
The application uses common web design conventions and is structured in an intuitive, easy to use way. Each page has a header and subtitle to clearly state its purpose and colour is used sparsly to increase both readability and keep the design clean.

The navigation bar has a logo on the left and the links to the right. When the screen size is too small to display the links, the menu turns into a collapsable menu with the familiar 'hamburger' icon.

The footer is at the bottom of the page and contains links to my Github page and a contact form.

The application contains the following pages:

- The index page with an introduction to the application and a brief overview of its features
- The sign up page where new users can create an account
- The log in page where users can log in to the application
- The log out page where logged in users can log out of the application
- The meal planner page where: 
    - Logged in users will see a weekly overview of their meal plans
    - The date of the first day can be picked to generate a new weekly schedule
    - New meal plans can be created by clicking on the '+' button to take users to the 'Add meal plan' page
    - Existing meal plans can be edited by clicking on the pen button to take users to the 'Edit meal plan' page
    - Existing meal plans can be deleted by clicking on the bin button, triggering a modal for confirmation, after which the meal plan will be deleted
- The create meal plan page where logged in users can create a new meal plan for the selected date, allowing up to 10 meals per meal plan
- The edit meal plan page where logged in users can edit an existing meal plan by changing or deleting meals from the plan
- The recipe list page where users can browse all recipes
    - Users can filter by meal type (breakfast, lunch, dinner, snack), diet type (vegetarian, vegan) or simply use the search bar
- The recipe page where logged in users can find the recipe ingredients and instructions and a picture of the finished meal
- The profile page where logged in users can find their username, first name, email address, creation date and a 'Delete account' button if they wish to have their profile delete
    - The 'Delete account' button triggers a modal for confirmation, after which the users' account and all its associated data will be deleted
- The contact page where users can contact me to leave feedback, report bugs, or simply send a message
    - Logged in users will have the 'Name' and 'E-mail address' fields pre-populated with their data and cannot be edited
- The 400, 403, 404 and 500 pages to handle HTTP responses and keep users inside the application flow

## Technical Design

### Database
The backend of the application is built with Python and the Django framework, with a PostgreSQL database attached via Heroku. The models in the meal and mealplanner app are used to create the entire database along with the models from Allauth.

<details><summary>Screenshot of database diagram</summary>
    <img src="docs/db-diagram.JPG">
</details>

### Database models

#### User model
The User model comes from the Allauth library and contains information about the user.

#### Calendar model
The Calendar model is used to create the weekly overview on the meal_planner page.
It contains the following fields:
- user
    - contains User as a foreign key
- picked_date
- day_one
- day_two
- day_three
- day_four
- day_five
- day_six
- day_seven

#### MealPlanner model
The MealPlanner model is used to save each users' meal plans.
It contains the following fields:
- user
    - contains User as a foreign key
- meal_plans
    - contains MealPlan as a many to many field

#### MealPlan model
The MealPlan model is used to save and contain all the meals that have been added to it.
It contains the following fields:
- meal_planner
    - contains MealPlanner as a foreign key
- date
- meal
    - contains Meal as a many to many field through MealToMealPlan

#### MealToMealPlan model
Is used as an intermediate model between the MealPlan and Meal models.
It contains the following fields:
- meal
    - contains Meal as a foreign key
- meal_plan
    - contains MealPlan as a foreign key

#### Meal model
Arguably the most important model as the whole application revolves around it. It is used to populate the meal plans, recipe list and recipe pages.
It contains the following fields:
- name
- image
- description
- ingredients
    contains Ingredient as a many to many field through IngredientToRecipe
- type
    - contains MealType as a foreign key
- diet
    - contains Diet as a foreign key
- prep_time
    - contains PrepTime as a foreign key
- cook_time
    - contains CookTime as a foreign key

#### IngredientToRecipe model
Is used as an intermediary model between the Meal and Ingredient models. The reason it is called 'IngredientToRecipe' and not 'IngredientToMeal' is because the ingredients are only used on the recipe page.
Contains the following fields:
- ingredient
    - contains Ingredient as a foreign key
- meal
    - contains Meal as a foreign key
- amount

#### Ingredient model
Is used to hold the ingredients that are used on the recipe pages.
Contains the following field:
- ingredient

#### MealType model
Is used to set the meal type of each meal.
Contains the following field:
- type

#### Diet model
Is used to set the diet type of each meal.
Contains the following field:
- diet

#### PrepTime model
Is used to set the prep time for each meal.
Contains the following field:
- prep_time

#### CookTime model
Is used to set the cook time for each meal.
Contains the following field:
- cook_time

### Wireframes

<details><summary>Home</summary>
    <img src="docs/wireframes/home-wireframe.png">
</details>

<details><summary>Login</summary>
    <img src="docs/wireframes/login-wireframe.png">
</details>

<details><summary>Logout</summary>
    <img src="docs/wireframes/logout-wireframe.png">
</details>

<details><summary>Create account</summary>
    <img src="docs/wireframes/create-account-wireframe.png">
</details>

<details><summary>Profile</summary>
    <img src="docs/wireframes/profile-wireframe.png">
</details>

<details><summary>Meal planner</summary>
    <img src="docs/wireframes/meal-planner-wireframe.png">
</details>

<details><summary>Create meal plan</summary>
    <img src="docs/wireframes/create-meal-plan-wireframe.png">
</details>

<details><summary>Edit meal plan</summary>
    <img src="docs/wireframes/edit-meal-plan-wireframe.png">
</details>

<details><summary>Delete meal plan</summary>
    <img src="docs/wireframes/delete-meal-plan-wireframe.png">
</details>

<details><summary>Recipe list</summary>
    <img src="docs/wireframes/recipe-list-wireframe.png">
</details>

<details><summary>Recipe</summary>
    <img src="docs/wireframes/recipe-wireframe.png">
</details>

<details><summary>Contact</summary>
    <img src="docs/wireframes/contact-wireframe.png">
</details>

## Technologies Used

### Languages
- [**HTML**](https://www.python.org/)
- [**CSS**](https://www.python.org/)
- [**JavaScript**](https://www.python.org/)
- [**Python 3.8.11**](https://www.python.org/)

### Framework
- [**Django 3.2.15**](https://www.djangoproject.com/)

### Tools & Libraries
- [**Git**](https://git-scm.com/) was used for version control
- [**GitHub**](https://github.com/) was used as a remote repository to store the all project files
- [**Gitpod**](https://gitpod.io/) was used as the IDE to write the project code
- [**Heroku**](https://dashboard.heroku.com/) was used to deploy the project
- [**PostgreSQL**](https://www.postgresql.org/) was used to store the project data, specifically the 'Heroku Postgres' add-on
- [**Google Fonts**](http://pep8online.com/) was used to supply the fonts for my project
- [**Font Awesome**](https://fontawesome.com/) was used to supply the icons for my project
- [**WC3's Markup Validation Service**](https://validator.w3.org/) was used to validate my HTML code
- [**W3C's CSS Validation Service**](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code
- [**JShint**](https://jshint.com/) was used to validate my JavaScript code
- [**PEP8**](http://pep8online.com/) was used to validate my Python code
- [**Coverage**](https://github.com/nedbat/coveragepy) was used to produce reports on my python unit tests
- [**Google Chrome's DevTools**](http://pep8online.com/) was used to benchmark the applications' performance, accessibility, best practices and SEO
- [**Wave WebAIM's web accessibility evaluation tool**](https://wave.webaim.org/) was used to validate my Python code
- [**Bootstrap 5.1**](https://getbootstrap.com/docs/5.1/getting-started/download/) was used for the application layout and some of the styling
- [**Cloudinary**](https://) was used to store static files
- [**Crispy Forms**](https://github.com/django-crispy-forms/django-crispy-forms) was used to nicely format the forms used in my project
- [**Crispy Bootstrap 5**](https://github.com/django-crispy-forms/crispy-bootstrap5) was used to install the Bootstrap 5 template pack for Crispy Forms
- [**Summernote**](https://github.com/summernote/django-summernote) was used for the meal description field on the admin page, allowing me to style the preparation instructions
- [**Allauth**](https://github.com/pennersr/django-allauth) was used to take care of the accounts in the project


## Features
The website has a total of 15 features:

### Logo and navigation bar
- Font Awesome icon combined with a Google Fonts font is used as the logo, placed on the left as is conventional
- Is present on every page
- Is responsive and works on all screen sizes
- Covers user story **23** and **24**

<details><summary>Screenshot of logo and navigation bar</summary>
    <img src="docs/features/logo-and-navbar.JPG">
    <img src="docs/features/logo-and-navbar-2.JPG">
    <img src="docs/features/logo-and-navbar-3.JPG">
</details>

### Footer
- At the bottom of the page as is conventional, using the same colour as the navigation bar for consistency
- Contains a link to my GitHub account, using a Font Awesome GitHub icon
- Contains a link to the contact page, using a matching Font Awesome icon
- Is present on every page
- Covers user story **21** and **24**

<details><summary>Screenshot of footer</summary>
    <img src="docs/features/footer.JPG">
</details>

### Flash messages
- Flash messages are displayed to users when performing any important action, like creating, editing or deleting a meal plan or logging into their account, providing them with meaningful feedback
- No screenshots provided here - all flash messages can be seen in action under [Manual Testing - User Stories](#manual-testing---user-stories)
- Covers user story **16**

### Home page
- Introduces users to the application
- Provides a brief overview of the applications' features
- Contains call-to-action buttons to the meal planner (if users logged in, otherwise a 'Create account' button is shown), recipe list and contact form
- Covers user story **1**, **18**

<details><summary>Screenshots of home page</summary>
    <img src="docs/features/home-page.JPG">
    <img src="docs/features/home-page-2.JPG">
    <img src="docs/features/home-page-3.JPG">
</details>

### Create account page
- Allows new users to create an account
- Users need to provide their email address, username, first name and a password
- The email address and username have to be unique
- All input is validated
- After their account has been created, Users are automatically logged in and taken to the meal planner page
- Flash message is displayed after account has been created
- Covers user story **3**, **22** and **16**

<details><summary>Screenshot of create account page</summary>
    <img src="docs/features/create-account-page.JPG">
</details>

### Login page
- Allows returning users to log in to their account
- Users need to enter their username and password - an empty or semi-empty form cannot be submitted
- All input is validated
- Users are taken to the meal planner page after successfully logging in
- Flash message is displayed after users have logged in
- Covers user story **4**, **22** and **16**

<details><summary>Screenshot of login page</summary>
    <img src="docs/features/login-page.JPG">
</details>

### Logout page
- Allows logged in users to log out of their account
- Flash message is displayed after users have logged out
- Covers user story **15** and **16**

<details><summary>Screenshot of logout page</summary>
    <img src="docs/features/logout-page.JPG">
</details>

### Profile page
- Allows users to view their account details, listing their username, first name, email address and creation date
- Allows users to delete their account should they wish to do so
    - Instead of a separate page, a modal is used to confirm if the user wishes to delete their account
- Flash message is displayed after users have deleted their account
- Covers user story **13**, **14** and **16**

<details><summary>Screenshot of profile page</summary>
    <img src="docs/features/profile-page.JPG">
</details>

### Meal planner page
- Provides users with a weekly overview of their meal plans
- Allows users to pick the first day of their weekly overview, allowing them to look back at past meal plans or plan ahead
- Provides a link to the 'Add meal plan' page
- Provides a link to the 'Edit meal plan' page
- Allows users to delete an existing meal plan
    - Instead of a separate page, a modal is used to confirm if the user wishes to delete a specific meal plan
    - Flash message is displayed after the user has deleted a specific meal plan
- Covers user story **8**, **9**, **10** and **16**

<details><summary>Screenshot of meal planner page</summary>
    <img src="docs/features/meal-planner-page.JPG">
</details>

### Create meal plan page
- Allows users to create a new meal plan for the selected date
- Allows users to add up to 10 meals
- Flash message is displayed after a meal plan has been created
- Covers user story **6** and **16**

<details><summary>Screenshots of create meal plan page</summary>
    <img src="docs/features/create-meal-plan-page.JPG">
    <img src="docs/features/create-meal-plan-page-2.JPG">
    <img src="docs/features/create-meal-plan-page-3.JPG">
</details>

### Edit meal plan page
- Allows users to edit their selected, existing meal plan
- Allows users to delete and add any available meal, limited to a maximum of 10 meals
- Flash message is displayed after a meal plan had been updated
- Covers user story **7** and **16**

<details><summary>Screenshots of edit meal plan page</summary>
    <img src="docs/features/edit-meal-plan-page.JPG">
    <img src="docs/features/edit-meal-plan-page-2.JPG">
    <img src="docs/features/edit-meal-plan-page-3.JPG">
</details>

### Recipe list page
- Allows both anonymous and registered users to browse all available recipes
- Provides a link to the recipes' page, which only registered, logged in users can access
- Covers user story **2**, **11**, **16** **18**

<details><summary>Screenshot of recipe list page</summary>
    <img src="docs/features/recipe-list-page.gif">
</details>

### Recipe page
- Contains the recipes' name preparation time, cooking time, meal type, diet type and image in the header
- Contains the recipes' ingredient list
- Contains the recipes' preparation instructions
- Provides a button to take users back to the recipe list
- Covers user story **12**

<details><summary>Screenshot of recipe page</summary>
    <img src="docs/features/recipe-page.png">
</details>

### Recipe list filter
- Allows both anonymous and registered users to filter all available recipes
- Users can filter by meal type (breakfast, lunch, dinner and snack)
- Users can filter by diet type (vegetarian, vegan)
- Users can filter by using the search bar
- Users can combine the meal type, diet type and search bar filters
- Covers user story **17**

<details><summary>Screenshot of recipe list filter</summary>
    <img src="docs/features/recipe-list-filter.gif">
</details>

### Contact page
- Allows both anonymous and registered, logged in users to send me a message via a contact form
- The contact form contains a name, email address and message field, all of which are required
- If a registered user is logged in, their name and email address are automatically added to the corresponding fields - the fields cannot be edited
- Flash message is displayed after the form has been successfully submitted
- Covers user story **20**, **22** and **16**

<details><summary>Screenshots of contact page</summary>
    <img src="docs/features/contact-page.JPG">
    <img src="docs/features/contact-page-2.JPG">
</details>

### Custom HTTP response pages (400, 403, 404 and 500)
- Keeps users in the application flow if they encounter an error by displaying a custom HTTP response page
- Contains a button that takes users back to the home page
- Covers user story **19**

<details><summary>Screenshot of custom HTTP response page 404</summary>
    <img src="docs/features/404-page.JPG">
</details>

## Validation

### HTML Validation
The HTML of the application has been validated using W3C's Markup Validation Service. all of the pages pass with no errors or warnings.

<details><summary>Screenshot of base template HTML validation</summary>
    <img src="docs/validation/html/base-template-html-validation.JPG">
</details>

<details><summary>Screenshot of index HTML validation</summary>
    <img src="docs/validation/html/index-html-validation.JPG">
</details>

<details><summary>Screenshot of login HTML validation</summary>
    <img src="docs/validation/html/login-html-validation.JPG">
</details>

<details><summary>Screenshot of logout HTML validation</summary>
    <img src="docs/validation/html/logout-html-validation.JPG">
</details>

<details><summary>Screenshot of create account HTML validation</summary>
    <img src="docs/validation/html/signup-html-validation.JPG">
</details>

<details><summary>Screenshot of profile HTML validation</summary>
    <img src="docs/validation/html/profile-html-validation.JPG">
</details>

<details><summary>Screenshot of meal planner page validation</summary>
    <img src="docs/validation/html/meal-planner-html-validation.JPG">
</details>

<details><summary>Screenshot of create meal plan HTML validation</summary>
    <img src="docs/validation/html/create-meal-plan-html-validation.JPG">
</details>

<details><summary>Screenshot of edit meal plan HTML validation</summary>
    <img src="docs/validation/html/edit-meal-plan-html-validation.JPG">
</details>

<details><summary>Screenshot of recipe list HTML validation</summary>
    <img src="docs/validation/html/recipe-list-html-validation.JPG">
</details>

<details><summary>Screenshot of recipe HTML validation</summary>
    <img src="docs/validation/html/recipe-html-validation.JPG">
</details>

<details><summary>Screenshot of contact HTML validation</summary>
    <img src="docs/validation/html/contact-html-validation.JPG">
</details>

### CSS Validation
The CSS of the application has been validated using W3C's CSS Validation Service. It passed with no errors or warnings.

<details><summary>Screenshot of CSS validation</summary>
    <img src="docs/validation/css/style-css-validation.JPG">
</details>

### JavaScript Validation
The JavaScript of the application has been validated using JSHint. It passed with no errors or warnings.

<details><summary>Screenshot of meal-planner.js JSHint validation</summary>
    <img src="docs/validation/js/meal-planner-jshint.JPG">
</details>

<details><summary>Screenshot of meal-search.js JSHint validation</summary>
    <img src="docs/validation/js/meal-search-jshint.JPG">
</details>

<details><summary>Screenshot of message-dismissal.js JSHint validation</summary>
    <img src="docs/validation/js/message-dismissal-jshint.JPG">
</details>

### Python Validation
The Python code has been validated using [Pep8 Validation Service](http://pep8online.com/) - no errors or warnings were found.

<details><summary>Screenshots of home Python files PEP8 Validation</summary>
    <details><summary>home views</summary>
        <img src="docs/validation/pep8/home-views-pep8-validation.JPG">
    </details>
    <details><summary>home urls</summary>
        <img src="docs/validation/pep8/home-urls-pep8-validation.JPG">
    </details>
    <details><summary>home forms</summary>
        <img src="docs/validation/pep8/home-forms-pep8-validation.JPG">
    </details>
</details>

<details><summary>Screenshots of meal Python files PEP8 Validation</summary>
    <details><summary>meal views</summary>
        <img src="docs/validation/pep8/meal-views-pep8-validation.JPG">
    </details>
    <details><summary>meal urls</summary>
        <img src="docs/validation/pep8/meal-urls-pep8-validation.JPG">
    </details>
    <details><summary>meal models</summary>
        <img src="docs/validation/pep8/meal-models-pep8-validation.JPG">
    </details>
    <details><summary>meal admin</summary>
        <img src="docs/validation/pep8/meal-admin-pep8-validation.JPG">
    </details>
</details>

<details><summary>Screenshots of mealplanner Python files PEP8 Validation</summary>
    <details><summary>mealplanner views</summary>
        <img src="docs/validation/pep8/mealplanner-views-pep8-validation.JPG">
    </details>
    <details><summary>mealplanner urls</summary>
        <img src="docs/validation/pep8/mealplanner-urls-pep8-validation.JPG">
    </details>
    <details><summary>mealplanner forms</summary>
        <img src="docs/validation/pep8/mealplanner-forms-pep8-validation.JPG">
    </details>
    <details><summary>mealplanner models</summary>
        <img src="docs/validation/pep8/mealplanner-models-pep8-validation.JPG">
    </details>
    <details><summary>mealplanner admin</summary>
        <img src="docs/validation/pep8/mealplanner-admin-pep8-validation.JPG">
    </details>
</details>

### Accessibility (Wave WebAIM)
The accessibility of the application has been measured using the Wave WebAIM web accessibility evaluation tool - all pages pass without errors.

<details><summary>Screenshot of index page accessibility evaluation</summary>
    <img src="docs/validation/wave/index-wave.JPG">
</details>

<details><summary>Screenshot of login page accessibility evaluation</summary>
    <img src="docs/validation/wave/login-wave.JPG">
</details>

<details><summary>Screenshot of logout page accessibility evaluation</summary>
    <img src="docs/validation/wave/logout-wave.JPG">
</details>

<details><summary>Screenshot of index page accessibility evaluation</summary>
    <img src="docs/validation/wave/index-wave.JPG">
</details>

<details><summary>Screenshot of create account page accessibility evaluation</summary>
    <img src="docs/validation/wave/signup-wave.JPG">
</details>

<details><summary>Screenshot of profile page accessibility evaluation</summary>
    <img src="docs/validation/wave/profile-wave.JPG">
</details>

<details><summary>Screenshot of meal planner page accessibility evaluation</summary>
    <img src="docs/validation/wave/meal-planner-wave.JPG">
</details>

<details><summary>Screenshot of create meal plan page accessibility evaluation</summary>
    <img src="docs/validation/wave/create-meal-plan-wave.JPG">
</details>

<details><summary>Screenshot of edit meal plan page accessibility evaluation</summary>
    <img src="docs/validation/wave/edit-meal-plan-wave.JPG">
</details>

<details><summary>Screenshot of recipe list page accessibility evaluation</summary>
    <img src="docs/validation/wave/recipe-list-wave.JPG">
</details>

<details><summary>Screenshot of recipe page accessibility evaluation</summary>
    <img src="docs/validation/wave/recipe-wave.JPG">
</details>

<details><summary>Screenshot of contact page accessibility evaluation</summary>
    <img src="docs/validation/wave/contact-wave.JPG">
</details>

### Performance (Google Lighthouse)
The performance of the application has been measured with Google Lighthouse with either a perfect or near perfect score on each page.

<details><summary>Screenshot of index page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/index-lighthouse.JPG">
</details>

<details><summary>Screenshot of login page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/login-lighthouse.JPG">
</details>

<details><summary>Screenshot of logout page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/logout-lighthouse.JPG">
</details>

<details><summary>Screenshot of create account page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/signup-lighthouse.JPG">
</details>

<details><summary>Screenshot of profile page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/profile-lighthouse.JPG">
</details>

<details><summary>Screenshot of meal planner page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/meal-planner-lighthouse.JPG">
</details>

<details><summary>Screenshot of create meal plan page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/create-meal-plan-lighthouse.JPG">
</details>

<details><summary>Screenshot of edit meal plan page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/edit-meal-plan-lighthouse.JPG">
</details>

<details><summary>Screenshot of recipe list page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/recipe-list-lighthouse.JPG">
</details>

<details><summary>Screenshot of recipe page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/recipe-lighthouse.JPG">
</details>

<details><summary>Screenshot of contact page Lighthouse performance</summary>
    <img src="docs/validation/lighthouse/contact-lighthouse.JPG">
</details>

## Testing

### Manual Testing - User Stories

1. As an anonymous user, I want to be able to view the home page, so I know what the application is about

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home page | Go to the [deployed application](https://ci-pp4-whatscooking.herokuapp.com/)  | Be informed about the applications' purpose and features | Works as expected |

<details><summary>Supporting Screenshots - User Story 1</summary>
    <img src="docs/testing/user-story-testing/user-stories-01.png">
</details>

2. As an anonymous user, I want to be able to view the recipe list, so I get a taste of what the application has to offer

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe list page | Click on the 'Recipe list' link in the navbar  | Be able to view the recipe list despite not having an account or being logged in | Works as expected |

<details><summary>Supporting Screenshots - User Story 2</summary>
    <img src="docs/testing/user-story-testing/user-stories-02.gif">
</details>

3. As an anonymous user, I want to be able to create an account, so I can start using the application

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create account page | Click on the 'Register' link in the navbar, the 'Create account' button on the homepage or the 'Create account' button on the recipe list page  | Be able to create an account | Works as expected |

<details><summary>Supporting Screenshots - User Story 3</summary>
    <img src="docs/testing/user-story-testing/user-stories-03.png">
</details>

4. As a registered user, I want to be able to log in with my account

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Login page | Click on the 'Log in' link in the navbar | Be able to log in to my account | Works as expected |

<details><summary>Supporting Screenshots - User Story 4</summary>
    <img src="docs/testing/user-story-testing/user-stories-04.png">
</details>

5. As a registered user, I want to be able to create a meal plan for a specific date 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page, add meal plan page | Click on the 'Meal planner' link in the navbar, then click any of the '+' buttons to create a meal plan for that date | Be able to create a meal plan | Works as expected |

<details><summary>Supporting Screenshots - User Story 5</summary>
    <img src="docs/testing/user-story-testing/user-stories-05.png">
</details>

6. As a registered user, I want to be able to add meals to a meal plan

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page, add meal plan page | Click on the 'Meal planner' link in the navbar, then click any of the '+' buttons to create a meal plan for that date, add meals to the meal plan | Be able to add meals to a meal plan | Works as expected |

<details><summary>Supporting Screenshots - User Story 6</summary>
    <img src="docs/testing/user-story-testing/user-stories-06.png">
</details>

7. As a registered user, I want to be able to edit any of my meal plans

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page, edit meal plan page | Click on the 'Meal planner' link in the navbar, then click on the pen button of the meal plan you want to edit | Be able to edit a meal plan | Works as expected |

<details><summary>Supporting Screenshots - User Story 7</summary>
    <img src="docs/testing/user-story-testing/user-stories-07.png">
</details>

8. As a registered user, I want to be able to delete any of my meal plans

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page | Click on the 'Meal planner' link in the navbar, then click any on the trash button of the meal plan you want to delete | Be able to delete a meal plan | Works as expected |

<details><summary>Supporting Screenshots - User Story 8</summary>
    <img src="docs/testing/user-story-testing/user-stories-08.png">
</details>

9. As a registered user, I want to have a weekly overview of my meal plans in my meal planner

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page | Click on the 'Meal planner' link in the navbar, then look at the weekly overview | Be able to see a weekly overview of meal plans | Works as expected |

<details><summary>Supporting Screenshots - User Story 9</summary>
    <img src="docs/testing/user-story-testing/user-stories-09.png">
</details>

10. As a registered user, I want to be able to pick the first day of the week of my weekly overview

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page | Click on the 'Meal planner' link in the navbar, then click on the calendar icon under 'Pick a date for day 1:', select a day, then click on the 'Pick day' button | Be able to see a new weekly overview, starting from the day I picked | Works as expected |

<details><summary>Supporting Screenshots - User Story 10</summary>
    <img src="docs/testing/user-story-testing/user-stories-10.png">
</details>

11. As an registered user, I want to be able to view the recipe list

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe list page | Click on the 'Recipe list' link in the navbar  | Be able to view the recipe list | Works as expected |

<details><summary>Supporting Screenshots - User Story 11</summary>
    <img src="docs/testing/user-story-testing/user-stories-11.gif">
</details>

12. As a registered user, I want to be able to view the details of each recipe in the recipe list

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe list page, recipe page | Click on the 'Recipe list' link in the navbar, then click on any of the recipes in the list | Be able to view the details of a recipe I clicked on | Works as expected |

<details><summary>Supporting Screenshots - User Story 12</summary>
    <img src="docs/testing/user-story-testing/user-stories-12.png">
</details>

13. As a registered user, I want to be able to view my account details on my profile page

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile page | Click on your username in the navbar to open a dropdown menu, click on the 'Profile' link | Be able to view my account details | Works as expected |

<details><summary>Supporting Screenshots - User Story 13</summary>
    <img src="docs/testing/user-story-testing/user-stories-13.png">
</details>

14. As a registered user, I want to be able to delete my account on my profile page

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile page | Click on your username in the navbar to open a dropdown menu, click on the 'Profile' link, then click on the 'Delete account button, confirm in the modal that you want to delete your account by clicking on the 'Yes, delete my account' button | Be able to delete my account | Works as expected |

<details><summary>Supporting Screenshots - User Story 14</summary>
    <img src="docs/testing/user-story-testing/user-stories-14.png">
</details>

15. As a registered user, I want to be able to log out when I'm done

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Logout page | Click on your username in the navbar to open a dropdown menu, click on the 'Log out' link | Be able to log out of my account | Works as expected |

<details><summary>Supporting Screenshots - User Story 15</summary>
    <img src="docs/testing/user-story-testing/user-stories-15.png">
</details>

16. As a registered user, I want to receive feedback after performing an important action

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home page, login page, log out page, contact page, meal planner page, create meal page, edit meal page | Perform an important action, like logging in or out, creating a new meal plan etc. | Have a flash message displayed | Works as expected, as can be seen on each individual feature - the feedback message is highlighted in the screenshots |

17. As the application owner, I want users to be able to filter recipes by meal type, diet type or by using the search bar

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe list page | Click on the checkboxes underneath 'Meal type', select an option underneath 'Diet type, use the search bar to find a recipe, or combine them | Be able to gilter recipes | Works as expected |

<details><summary>Supporting Screenshots - User Story 17</summary>
    <img src="docs/testing/user-story-testing/user-stories-17.gif">
</details>

18. As the application owner, I want to restrict most of the applications' functionality for anonymous users to encourage them to create an account

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Meal planner page, recipe page | Look at the navbar or try to open a recipe when not logged in | Have no meal planner option and be unable to open a recipe - will redirect to the login page | Works as expected |

<details><summary>Supporting Screenshots - User Story 18</summary>
    <img src="docs/testing/user-story-testing/user-stories-18.png">
</details>

19. As the application owner, I want users to stay on the application when they receive an HTTP response of 400, 403, 404 or 500

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Custom HTTP response page 404 | Enter a non-existing page name at the end of the apps' url | Have a custom 404 error page be displayed | Works as expected |

<details><summary>Supporting Screenshots - User Story 19</summary>
    <img src="docs/testing/user-story-testing/user-stories-19.png">
</details>

20. As the application owner, I want users to be able to contact me with a contact form

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home page, footer, contact page | Scroll down on the home page and click on the 'Contact us' button or scroll down on any page and click the envelope icon in the footer | Be able to submit a contact form | Works as expected |

<details><summary>Supporting Screenshots - User Story 20</summary>
    <img src="docs/testing/user-story-testing/user-stories-20.png">
</details>

21. As the application owner, I want users to be able to find me on GitHub

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer | Scroll down on any page and click the GitHub icon in the footer | Open a new tab to my GitHub page | Works as expected |

<details><summary>Supporting Screenshots - User Story 21</summary>
    <img src="docs/testing/user-story-testing/user-stories-21.png">
</details>

22. As the application owner, I want the users' input on forms to be validated

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Login page, logout page, create account page, contact page | Try to submit form without filling out the required fields or enter invalid data, like a partial email address | Have a warning message display and be unable to submit the form | Works as expected |

<details><summary>Supporting Screenshots - User Story 22</summary>
    <img src="docs/testing/user-story-testing/user-stories-22.png">
</details>

23. As the application owner, I want users to be able to navigate around the application easily

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any page | Click on the corresponding link in the navbar, or the corresponding buttons on a parent page | Be taken to the correct page | Works as expected, as can be seen in all of the feature screenshots |

24. As the application owner, I want to provide a responsive application for all devices

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| The whole application | Resize any page | Have the page be formatted correctly for any device | Works as expected |

<details><summary>Supporting Screenshots - User Story 24</summary>
    <img src="docs/testing/user-story-testing/user-stories-24.png">
</details>

### Automated Testing
Some automated testing was carried out with by using Pythons' built-in unittest library. The screenshots that I added below are from the reports that were created by using coverage.

<details><summary>Screenshot of home app coverage report</summary>
    <img src="docs/testing/automated-testing/home-app-coverage.JPG">
</details>

<details><summary>Screenshot of mealplanner app coverage report</summary>
    <img src="docs/testing/automated-testing/mealplanner-app-coverage.JPG">
</details>

<details><summary>Screenshot of meal app coverage report</summary>
    <img src="docs/testing/automated-testing/meals-app-coverage.JPG">
</details>

## Bugs

| **Bug** | **Fix** |
|-------------|------------|
| Contact form too big when logged in, styling not consistent | Change column size of name field from md-6 to md-12 to take up the whole column, add input tag to styling rule - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/72a0265165d5f268da9294682a54148d3e646b83) |
| Icons in footer too small | Change styling rule to specifically target anchor elements inside the list that holds them - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/f675d6e670f704c991d89c7e47fd351ff9212b0d) |
| Bootstrap modal stopped working after upgrading to Bootstrap 5 | Change data attributes to data-bs attributes - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/ae6d3a697633fce0221e9161807ca6727679e013) |
| Footer not at the bottom of the page if content doesn't push it down | Set body height to 100vh, display to flex and flex direction to column. Then set the footers' margin-top to auto - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/dc9817898a00dc3897e3df5b1b55182968cbee02) |
| Footer not at the bottom of the page if content doesn't push it down | Set body height to 100vh, display to flex and flex direction to column. Then set the footers' margin-top to auto - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/dc9817898a00dc3897e3df5b1b55182968cbee02) |
| Scripts not working properly | Accidentally had scripts outside of body tag, moved them inside - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/86a6a877206f0e83210bc50f519b043636424529) |
| CreateMealPlan view doesn't grab the correct meal planner when creating a meal plan | Used the wrong user attribute, change from user.username to user.id - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/40a225901d82bec44120a31d6776c192fb649493) |
| Diet filter not working anymore | Accidentally deleted span that is used to target the right recipes, add it back in - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/5855ac3cc0d22d28b797a9b537615c78c579c821) |
| Meal plans can no longer be created | Crispy forms required a different set up to work properly with my form and formset, added proper formartting to make it work again - [link to commit](https://github.com/vkleer/CI_PP4_WhatsCooking/commit/bbebbab02991cba2a142e6377ea4b2235b3241df) |


## Deployment

### GitHub
This website was deployed using Github Pages with the following steps:

1. Go to your Github Repository
2. Navigate to the 'Settings' page
3. On the left hand menu under 'Code and automationo', click on 'Pages'
4. Under 'Source', click on the 'Branch' dropdown element and set it to your main branch (in my case, this branch is called 'main')
5. Click on 'Save'
6. Refresh the page and you will be provided with a link to your deployed Github Page.

If you want to fork this repository, follow these steps:

1. Go to the Github repository (https://github.com/vkleer/CI_PP4_WhatsCooking)
2. Click on the 'Fork' button in the top right corner under the navigation bar

If you want to clone this repository, follow these steps:

1. Go to the Github repository (https://github.com/vkleer/CI_PP4_WhatsCooking)
2. Click on the 'Code' button above the list of files
3. Select your preferred way of cloning, I recommend using the 'GitHub CLI' option
4. Under 'GitHub CLI', click on the copy button to copy the clone command
5. In you IDE, open Git Bash
6. Navigate to the working directory where you want to clone this directory
7. Paste in the clone command you copied and press the 'enter' key to create the clone

### Heroku
This application has been deployed using Heroku with the following steps:

1. Login to [Heroku](https://id.heroku.com/login)
1. Go to your Heroku dashboard
3. In the top-right corner, click on the 'New' button, followed by the 'Create a new app' button
4. Enter an app name (it has to be unique) and choose your region under the 'Choose a region' dropdown menu.
5. Click on the 'Create app' button
6. On the next page, click on the 'Settings' tab 
7. Under 'Config Vars', click on 'Reveal Config Vars' to add a new Config var - this is where you can store sensitive data, like your Google service account key
8. Under 'Buildpacks' click on the 'Add buildpack' button to install additional dependencies. For this project the 'python' and 'nodejs' buildpacks were added, in that specific order
9. Click on the 'Deploy' tab
10. Under 'Deployment method', click on 'Github'. You can then search for your repository under 'Search for a repository to connect to'
11. Click on the 'Connect' button to connect your repository
12. On the next page, under 'Choose a branch to deploy' you can choose the branch you want to deploy your app from
13. Either click on the 'Enable Automatic Deploys' button under 'Automatic deploys' to have the app deploy automatically on each push you make to the branch, or click on the 'Deploy Branch' button under 'Manual deploy'
14. Wait for the app to build and be deployed. Once the app is ready, a message will be displayed saying 'App was successfully deployed' along with a button which takes you to your newly deployed app

### Google SMTP Server
To send emails from your website using Google's SMTP server, the following steps are required:

1. Preferable, create a new Gmail account
2. Following the instructions in [this link](https://support.google.com/accounts/answer/6010255?hl=en), enable the less secure apps feature
3. Under your settings.py, add the following settings:
    - EMAIL_BACKEND = ???django.core.mail.backends.smtp.EmailBackend???
    - EMAIL_HOST = ???smtp.gmail.com???
    - EMAIL_USE_TLS = True
    - EMAIL_PORT = 587
    - EMAIL_HOST_USER = ???your_account@gmail.com??? (I set this up in my env.py file and grab the variables using os.environ.get)
    - EMAIL_HOST_PASSWORD = ???your account???s password???(Again, this is set up in my env.py file and the variables are grabbed using os.environ.get)
4. On Heroku, under settings, add two new Config Vars: EMAIL_HOST_USER and EMAIL_HOST_PASSWORD, using the same email address and password

## Credits

### Images
- All images and the recipes themselves were found on [BBC Food](https://www.bbc.co.uk/food/recipes/)

### Code
- I wasn't quite sure how to structure my ingredients model, but [this post from Stackoverflow](https://stackoverflow.com/questions/70142026/how-to-handle-recipe-ingredients-in-databases) helped me figure it out
- My ManyToMany fields weren't showing up on my admin panel, [this post from Stackoverflow](https://stackoverflow.com/questions/70118016/django-many-to-many-field-not-showing-on-admin-legacy-database) was very helpful
- I wanted to add extra fields to my sign up form, which I was able to do thanks to [this post from Stackoverflow](https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth)
- I was struggling to get next and previous days for my calendar, but [this article](https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/) helped me figure it out
- I wanted to set the intial field values of some forms to something specific, but didn't know how - [this post from Stackoverflow] was very helpful
- Though I had looked at project examples, I didn't quite understand how inline formsets worked - [this video on YouTube](https://www.youtube.com/watch?v=MRWFg30FmZQ) was really a life saver
- I wanted to disable some of my form fields by default, that was possible thanks to [this post on Stackoverflow](https://stackoverflow.com/questions/66106617/how-to-use-field-disabled-in-django)
- I wanted anonymous users to be able to browse the recipe list, but not be able to open the actual recipe page. Luckily I found out that you can add a login decorator, thanks to [this post from Stackoverflow](https://stackoverflow.com/questions/68810221/login-required-decorator-gives-object-has-no-attribute-user-error)
- To set up the contact form, I looked at some other users' projects and browsed the web for a good solution - in the end I decided to use Google SMTP, which was help set up thanks to [this article on Medium](https://bshoo.medium.com/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e)


## Acknowledgements
I would like to thank:
- My mentor Mo Shami for providing me with advice and guidance for this project
- My partner Lauren Baker for helping me with testing and finding multiple bugs in the program
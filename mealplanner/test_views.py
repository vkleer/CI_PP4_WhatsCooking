from django.test import TestCase
from django.contrib.auth.models import User


class TestMealplannerView(TestCase):
    """
    A class to test the MealPlannerView view
    """
    def setUp(self):
        """
        Creates a test user
        """
        user = User.objects.create_user(
            username='user',
            password='lAZK3iY0*sDn82',
            email='user@test.com')
        user.save()
    
    def test_get_mealplanner_page(self):
        """
        Checks if the MealPlannerView page is displayed
        """
        self.client.login(username='user', password='lAZK3iY0*sDn82')
        response = self.client.get('/mealplanner/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meal_planner.html')


class TestCreateMealPlanView(TestCase):
    """
    A class to test the CreateMealPlan view
    """
    def setUp(self):
        """
        Creates a test user
        """
        user = User.objects.create_user(
            username='user',
            password='lAZK3iY0*sDn82',
            email='user@test.com')
        user.save()

    def test_create_meal_plan_page(self):
        """
        Checks if the create_meal_plan page is displayed
        """
        response = self.client.get('/mealplanner/create_meal_plan/2022-09-24')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_meal_plan.html')

from django.test import TestCase


class TestMealListView(TestCase):
    """
    A class to test the MealList view
    """
    def test_get_meals_page(self):
        """
        Checks if the meals page is displayed
        """
        response = self.client.get('/meals/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals.html')

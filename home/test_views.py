from django.test import TestCase
from django.contrib.auth.models import User


class TestHomePageView(TestCase):
    """
    A class to test the HomePage view
    """
    def test_get_home_page(self):
        """
        Checks if the index page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestContactView(TestCase):
    """
    A class to test the Contact view
    """
    def test_get_contact_page(self):
        """
        Checks if the contact page is displayed
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


class TestProfileView(TestCase):
    """
    A class to test the UserProfile view
    """
    def setUp(self):
        """
        Creates two test users
        """
        user = User.objects.create_user(
            username='user',
            password='lAZK3iY0*sDn82',
            email='user@test.com')
        user.save()
        other_user = User.objects.create_user(
            username='other_user',
            password='M1y5pCfZ^KQ1PG',
            email='other-user@test.com')
        other_user.save()
    
    def test_get_profile_page(self):
        """
        Checks if the profile page is displayed
        """
        self.client.login(username='user', password='lAZK3iY0*sDn82')
        response = self.client.get('/profile/user/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        User.objects.all().delete()
    
    def test_unauthorized_profile_page(self):
        """
        Checks if going to a profile page that's not your own gives
        the correct HTTP response
        """
        self.client.login(username='user', password='lAZK3iY0*sDn82')
        response = self.client.get('/profile/other_user/')
        self.assertEqual(response.status_code, 302)
        User.objects.all().delete()

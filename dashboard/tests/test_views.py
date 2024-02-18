from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class DashboardOverviewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = Client()
        self.client.login(username='test_user', password='test_password')

    def test_dashboard_overview_view(self):
        response = self.client.get(reverse('dashboard:dashboard_overview'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'dashboard/dashboard_overview.html')

    def test_dashboard_overview_requires_login(self):
        self.client.logout()

        response = self.client.get(reverse('dashboard:dashboard_overview'))

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, '/accounts/login/?next=/dashboard/dashboard/')


class EditMyAccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password', email='test@example.com',
            first_name='John', last_name='Doe'
        )

        self.client = Client()
        self.client.login(username='test_user', password='test_password')

    def test_edit_myaccount_view_get(self):
        response = self.client.get(reverse('dashboard:edit_myaccount'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'dashboard/edit_myaccount.html')

    def test_edit_myaccount_view_post(self):

        data = {
            'first_name': 'Updated First Name',
            'last_name': 'Updated Last Name',
            'email': 'updated_email@example.com',
            'username': 'updated_username'
        }

        response = self.client.post(reverse('dashboard:edit_myaccount'), data)

        self.assertEqual(response.status_code, 302)  

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated First Name')
        self.assertEqual(self.user.last_name, 'Updated Last Name')
        self.assertEqual(self.user.email, 'updated_email@example.com')
        self.assertEqual(self.user.username, 'updated_username')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Account Updated! Your changes have been saved.")

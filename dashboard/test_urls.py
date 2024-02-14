from django.test import TestCase
from django.urls import reverse, resolve
from dashboard.views import dashboard_overview, edit_myaccount

class DashboardUrlsTest(TestCase):
    def test_dashboard_overview_url_resolves(self):
        url = reverse('dashboard:dashboard_overview')
        self.assertEqual(resolve(url).func, dashboard_overview)
    
    def test_edit_myaccount_url_resolves(self):
        url = reverse('dashboard:edit_myaccount')
        self.assertEqual(resolve(url).func, edit_myaccount)
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from dashboard.views import dashboard_overview
from allauth.account.views import LoginView 


class TestUrls(TestCase):
    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, AdminSite().index.__name__)

    def test_mainshop_url(self):
        url = reverse('main_page')
        self.assertEqual(url, '/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'main_page')

    def test_cart_url(self):
        url = reverse('cart')
        self.assertEqual(url, '/cart/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'cart')

    def test_order_url(self):
        url = reverse('start_order')
        self.assertEqual(url, '/order/start_order/')

    def test_dashboard_url(self):
        url = reverse('dashboard:dashboard_overview')
        self.assertEqual(url, '/dashboard/dashboard/') 

    def test_login_url(self):
        url = reverse('account_login')
        self.assertEqual(url, '/accounts/login/')  
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, LoginView)

    def test_debug_media_url(self):
        if settings.DEBUG:
            url = settings.MEDIA_URL + 'test_image.jpg'
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)


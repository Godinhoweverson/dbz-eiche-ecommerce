from django.test import TestCase
from django.urls import reverse, resolve
from order.views import start_order

class TestStartOrderURL(TestCase):
    def test_start_order_url(self):
        url = reverse('start_order')
        self.assertEqual(url, '/order/start_order/')

        resolver = resolve(url)
        self.assertEqual(resolver.func, start_order)        

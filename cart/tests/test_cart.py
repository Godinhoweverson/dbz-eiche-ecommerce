from django.test import TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from mainshop.models import Product
from .cart import Cart

class CartTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.product = Product.objects.create(
            product_display_name="Test Product",
            price=10.00
        )
        self.request = self.factory.get('/')
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(self.request)
        self.request.session.save()
        self.cart = Cart(self.request)

    def test_add_product_to_cart(self):
        self.cart.add(self.product.id)
        self.assertEqual(len(self.cart), 1)

    def test_increment_quantity(self):
        self.cart.add(self.product.id)
        self.cart.increment_quantity(self.product.id)
        self.assertEqual(self.cart.cart[str(self.product.id)]['quantity'], 2)

    def test_decrement_quantity(self):
        self.cart.add(self.product.id)
        self.cart.decrement_quantity(self.product.id)
        self.assertEqual(self.cart.cart.get(str(self.product.id), {}).get('quantity', 0), 0)

    def test_remove_item_from_cart(self):
        self.cart.add(self.product.id)
        self.cart.remove_item(self.product.id)
        self.assertEqual(len(self.cart), 0)

    def test_get_total_cost(self):
        self.cart.add(self.product.id)
        total_cost = self.cart.get_total_cost()
        self.assertEqual(total_cost, 10.00)

    def test_get_item(self):
        self.cart.add(self.product.id)
        item = self.cart.get_item(self.product.id)
        self.assertIsNotNone(item)
        self.assertEqual(item['quantity'], 1)

from django.test import TestCase
from django.contrib.auth.models import User
from mainshop.models import Product
from order.models import Order, OrderItem

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='password')

    def setUp(self):
        self.order = Order.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            address='123 Main St',
            zipcode='12345',
            place='City',
            phone='1234567890',
            payment_intent='pi_test',
            paid=True,
            paid_amount=5000,
            status=Order.DELIVERED
        )

    def test_get_total_price_paid(self):
        self.assertEqual(self.order.get_total_price(), 50.00)

    def test_get_total_price_unpaid(self):
        self.order.paid = False
        self.order.save()
        self.assertNotEqual(self.order.get_total_price(), 0)

class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(product_display_name='Test Product', price=1000)

    def setUp(self):
        self.order_item = OrderItem.objects.create(
            order=Order.objects.create(),
            product=self.product,
            price=2000,
            quantity=2
        )

    def test_get_total_price(self):
        self.assertEqual(self.order_item.get_total_price(), 20.00)

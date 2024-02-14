from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from order.models import Order, OrderItem
from order.admin import OrderAdmin, OrderItemInline


class TestOrderAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.order_admin = OrderAdmin(Order, self.site)
        self.user = User.objects.create_user(username='admin', password='password')
        self.client.force_login(self.user)
        self.request_factory = RequestFactory()

    def test_order_admin_list_display(self):
        self.assertEqual(self.order_admin.list_display, ['id', 'status', 'created_at'])

    def test_order_admin_list_filter(self):
        self.assertEqual(self.order_admin.list_filter, ['status', 'created_at'])

    def test_order_admin_search_fields(self):
        self.assertEqual(self.order_admin.search_fields, ['first_name', 'address'])

class TestOrderItemInline(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.order_item_inline = OrderItemInline(Order, self.site)
        self.user = User.objects.create_user(username='admin', password='password')
        self.client.force_login(self.user)
        self.request_factory = RequestFactory()

    def test_order_item_inline_model(self):
        self.assertEqual(self.order_item_inline.model, OrderItem)

    def test_order_item_inline_raw_id_fields(self):
        self.assertEqual(self.order_item_inline.raw_id_fields, ['product'])

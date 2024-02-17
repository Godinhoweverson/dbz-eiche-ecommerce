from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from mainshop.models import Category, Product, Comment

class UrlsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories='Test Category')
        self.product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',
            season='Summer',
            description_product='Test Description',
            price=10.00,
            category=self.category,
            slug='test-product'
        )
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.comment = Comment.objects.create(user=self.user, product=self.product, text='Test Comment')

    def test_search_url(self):
        response = self.client.get(reverse('search'), {'q': 'your_search_term'})
        self.assertEqual(response.status_code, 200)
        self.comment = Comment.objects.create(
            product=self.product,
            text='Test Comment',
            approved_comment=True
        )

    def test_main_page_url(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_main_page_category_url(self):
        response = self.client.get(reverse('main_page_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_details_products_url(self):
        response = self.client.get(reverse('details_products', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_comment_url(self):
        response = self.client.get(reverse('edit_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_comment_url(self):
        response = self.client.get(reverse('delete_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_url(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)
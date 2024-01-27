from django.test import unnittest
from django.urls import reverse
from django.core.paginator import Paginator
from mainshop.views import main_page
from mainshop.models import Category, Product
from .utils import make_pagination_range

class MainPageViewTest(unnittestTestCase):

    def setUp(self):
        # Create some test data (categories and products) for your view
        self.category = Category.objects.create(display_categories='Test Category')
        self.product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',
            season='Summer',
            description_product='Test Description',
            price=20.99,
            color='Blue',
            category=self.category,
            slug='test-product'
        )

    def test_main_page_view_with_category_id(self):
        # Test the view when a category_id is provided
        response = self.client.get(reverse('main_page', kwargs={'category_id': self.category.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main.html')
        self.assertContains(response, 'Test Category')  # Check if the category is in the response
        self.assertContains(response, 'Test Product')  # Check if the product is in the response
        # Add more assertions as needed

    def test_main_page_view_without_category_id(self):
        # Test the view when no category_id is provided
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main.html')
        self.assertContains(response, 'Test Category')  # Check if the category is in the response
        self.assertContains(response, 'Test Product')  # Check if the product is in the response
        # Add more assertions as needed

    def test_main_page_pagination(self):
        # Test pagination in the view
        # Create more products to ensure pagination is working
        for _ in range(10):
            Product.objects.create(
                product_display_name='Another Product',
                gender='Male',
                season='Summer',
                description_product='Another Description',
                price=10.99,
                color='Red',
                category=self.category,
                slug='another-product'
            )
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main.html')
        self.assertContains(response, 'Test Category')  # Check if the category is in the response
        self.assertContains(response, 'Test Product')  # Check if the initial product is in the response
        self.assertContains(response, 'Another Product')  # Check if another product is in the response
        self.assertIsInstance(response.context['products'], Paginator)
        self.assertEqual(response.context['products'].num_pages, 2)  # Assuming 8 products per page
        # Add more assertions as needed

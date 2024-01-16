from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from mainshop.models import Category, Product

class MainshopUrlsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories='Test Category')

        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        self.product = Product.objects.create(
            product_display_name='Test Product',
            description_product='Test Description',
            price=10.0,
            category=self.category,
            image=image  
        )

    def test_main_page_url(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_main_page_category_url(self):
        response = self.client.get(reverse('main_page_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_details_products_url(self):
        response = self.client.get(reverse('details-products', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_product_search_url_is_correct(self):
        url = reverse('search')
        self.assertEqual(url, '/products/search/')
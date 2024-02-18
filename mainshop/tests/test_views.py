import unittest
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.core.files.uploadedfile import SimpleUploadedFile


from mainshop.models import Category, Product, Comment

from mainshop.views import main_page, details_products


# main_page
class MainShopViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories='Test Category')
        self.product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',  
            season='Summer',  
            description_product='Description', 
            price=10.00, 
            category=self.category,
            image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        )


    def test_main_page(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main.html')
        self.assertIn('categories', response.context)
        self.assertIn('products', response.context)
        self.assertIn('pagination_range', response.context)
        categories = response.context['categories']
        products = response.context['products']
        self.assertIn(self.category, categories)
        self.assertIn(self.product, products)

    def test_main_page_with_category(self):
        response = self.client.get(reverse('main_page'), {'category_id': self.category.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/main.html')
        self.assertIn('categories', response.context)
        self.assertIn('products', response.context)
        self.assertIn('pagination_range', response.context)
        categories = response.context['categories']
        products = response.context['products']
        self.assertIn(self.category, categories)
        self.assertIn(self.product, products)

# details_product

class DetailsProductsViewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories='Test Category')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.product = Product.objects.create(
            product_display_name='Test Product',
            gender='male',
            season='summer',
            description_product='Test description',
            price=100.00,
            color='red',
            category=self.category,
            slug='test-product',
        )
        self.comment = Comment.objects.create(user=self.user, product=self.product, text='Test comment')

    def test_details_products_view(self):
        url = reverse('details_products', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/details_product.html')
        self.assertContains(response, self.product.product_display_name)
        self.assertContains(response, self.comment.text)

    def test_post_comment(self):
        url = reverse('details_products', args=[self.product.id])
        post_data = {
            'text': 'New comment',
        }
        self.client.login(username='testuser', password='password123')
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(user=self.user, product=self.product, text='New comment').exists())

# edit_comment && delete

class EditDeleteCommentViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories='Test Category')
        self.product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',
            season='Summer',
            description_product='Test Description',
            price=100.00,
            category=self.category
        )
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.comment = Comment.objects.create(
            user=self.user,
            product=self.product,
            text='Test Comment',
            approved_comment=True
        )
        self.edit_comment_url = reverse('edit_comment', kwargs={'comment_id': self.comment.id})
        self.delete_comment_url = reverse('delete_comment', kwargs={'comment_id': self.comment.id})

    def test_edit_comment_view_get(self):
        response = self.client.get(self.edit_comment_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global/partials/edit_comment.html')

    def test_edit_comment_view_post(self):
        updated_text = 'Updated Test Comment'
        response = self.client.post(self.edit_comment_url, {'text': updated_text})
        self.assertEqual(response.status_code, 302)  # Redirect
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.text, updated_text)

    def test_delete_comment_view_post(self):
        response = self.client.post(self.delete_comment_url)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())
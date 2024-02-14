from django.contrib import admin
from django.test import TestCase
from .admin import CategoryAdmin, ProductAdmin, CommentAdmin
from .models import Category, Product, Comment
from django.contrib.auth.models import User

class TestAdmin(TestCase):
    def setUp(self):
        self.category = Category.objects.create(display_categories="Test Category")
        self.product = Product.objects.create(
            product_display_name="Test Product",
            gender="male",
            season="winter",
            description_product="Test description",
            price=10.00,
            color="Black",
            image="test_image.jpg",
            category=self.category,
            slug="test-product"
        )
        # Create a test user
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password")
        self.comment = Comment.objects.create(
            user=self.user,  # Use the test user instance
            email="test@example.com",
            text="Test comment",
            approved_comment=True,
            created_at="2022-02-13 10:00:00"
        )

    def test_category_admin(self):
        category_admin = CategoryAdmin(Category, admin.site)
        self.assertIn('display_categories', category_admin.list_display)

    def test_product_admin(self):
        product_admin = ProductAdmin(Product, admin.site)
        self.assertIn('product_display_name', product_admin.list_display)
        self.assertIn('gender', product_admin.list_display)
        self.assertIn('season', product_admin.list_display)
        self.assertIn('description_product', product_admin.list_display)
        self.assertIn('price', product_admin.list_display)
        self.assertIn('color', product_admin.list_display)
        self.assertIn('image', product_admin.list_display)
        self.assertIn('category', product_admin.list_display)
        self.assertIn('slug', product_admin.list_display)

    def test_comment_admin(self):
        comment_admin = CommentAdmin(Comment, admin.site)
        self.assertIn('user', comment_admin.list_display)
        self.assertIn('email', comment_admin.list_display)
        self.assertIn('text', comment_admin.list_display)
        self.assertIn('approved_comment', comment_admin.list_display)
        self.assertIn('created_at', comment_admin.list_display)

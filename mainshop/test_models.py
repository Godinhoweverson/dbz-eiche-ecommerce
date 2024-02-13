from django.test import TestCase
from .models import Category, Product, Comment
from django.contrib.auth.models import User

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.category = Category.objects.create(display_categories='Test Category')
        cls.product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',
            season='Summer',
            description_product='Test Description',
            price=10.00,
            category=cls.category,
            slug='test-product'
        )
    def test_category_str(self):
        category = Category.objects.create(display_categories='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_product_str(self):
        slug = 'test-product-1'
        product = Product.objects.create(
            product_display_name='Test Product',
            gender='Male',
            season='Winter',
            description_product='Test Description',
            price=10.50,
            category=self.category,
            slug=slug
        )
        self.assertEqual(str(product), 'Test Product')

    def test_comment_str_with_user(self):
        comment_text = "This is a test comment with a specified product"
        comment = Comment.objects.create(
            text=comment_text,
            user=self.user,
            product=self.product
        )

        self.assertEqual(str(comment), f'Comment {comment_text} by testuser')
        self.assertEqual(comment.product, self.product)

    def test_comment_likes_count(self):
        comment = Comment.objects.create(
            text="Test comment for likes count",
            user=self.user,
            product=self.product
        )
        comment.likes.add(self.user)
        self.assertEqual(comment.likes_count(), 1)
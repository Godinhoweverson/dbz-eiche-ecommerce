from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    display_categories = models.CharField(max_length=25)

    def __str__(self):
        return self.display_categories


class Product(models.Model):
    product_display_name = models.CharField(max_length=165)
    gender = models.CharField(max_length=5)
    season = models.CharField(max_length=10)
    description_product = models.CharField(max_length=165)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=12, null=True, blank=True)
    image = models.ImageField(upload_to='',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, default='Null')

    def to_json_serializable(self):
        product_dict = model_to_dict(self)
        product_dict['price'] = str(self.price)

        return product_dict


    def __str__(self):
        return self.product_display_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    text = models.TextField(max_length=200)
    approved_comment = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='like_comment', blank=True)

    def __str__(self):
        if self.user:
            return f'Comment {self.text} by {self.user.username}'
        return f'Comment {self.text} by Anonymous'

    def likes_count(self):
        return self.likes.count()





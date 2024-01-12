from django.db import models


class Category(models.Model):
    display_categories = models.CharField(max_length=25)

    def __str__(self):
        return self.display_categories


class Product(models.Model):
    product_display_name = models.CharField(max_length=165)
    gender = models.CharField(max_length=5)
    season = models.CharField(max_length=10)
    description_product = models.CharField(max_length=165)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=12, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product_display_name


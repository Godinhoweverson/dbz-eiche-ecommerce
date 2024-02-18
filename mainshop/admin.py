from django.contrib import admin
from .models import Category, Product, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_categories',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_display_name',
        'gender',
        'season',
        'description_product',
        'price',
        'color',
        'image',
        'category',
        'slug',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'text',
        'approved_comment',
        'created_at',

    )

# Generated by Django 3.2.23 on 2024-01-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='Null', unique=True),
        ),
    ]
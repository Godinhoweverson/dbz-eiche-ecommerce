# Generated by Django 3.2.23 on 2024-02-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
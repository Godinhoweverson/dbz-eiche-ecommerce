from django.urls import path
from mainshop.views import main_page, details_product

urlpatterns = [
    path('', main_page, name='main_page'),
    path('details', details_product, name='details-products'),
]
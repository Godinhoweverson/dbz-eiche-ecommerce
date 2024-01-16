from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/search/', views.search, name='search'),
    path('category/<int:category_id>/', views.main_page, name='main_page_category'),
    path('details/<int:product_id>/', views.details_products, name='details-products'),
]
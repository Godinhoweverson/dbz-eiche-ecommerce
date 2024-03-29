from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/search/', views.search, name='search'),
    path('category/<int:category_id>/', views.main_page, name='main_page_category'),
    path('details/<int:product_id>/', views.details_products, name='details_products'),
    path('comment/edit/<int:comment_id>/',views.edit_comment,name='edit_comment'),
    path('comment/delete/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
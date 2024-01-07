from django.urls import path
from mainshop.views import main_page

urlpatterns = [
    path('', main_page)
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit_myaccount/', views.edit_myaccount, name='edit_myaccount'),
]
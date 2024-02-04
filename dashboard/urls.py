from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard_overview, name='dashboard_overview'),
    path('edit_myaccount', views.edit_myaccount, name='edit_myaccount'),
   
]
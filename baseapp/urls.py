from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('footage/<str:pk>/', views.footage, name='footage'),
]
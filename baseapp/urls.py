from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('footage/<str:pk>/', views.footage, name='footage'),
    path('footage/delete/<str:pk>/', views.delete_footage, name='footage'),
    path('date/', views.find_footage, name='find_footage'),

]
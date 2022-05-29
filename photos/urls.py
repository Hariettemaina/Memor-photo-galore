from django.urls import path
from .import views



urlpartterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('', views.gallery, name='gallery')
]
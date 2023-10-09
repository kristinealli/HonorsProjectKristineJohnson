from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('items/', views.items, name='items'),
    path('items/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
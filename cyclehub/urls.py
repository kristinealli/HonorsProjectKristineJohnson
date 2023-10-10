from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.main, name='main'),
    path('items/', views.items, name='items'),
    path('all_items/', views.items, name='all_items'),
    path('items/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('add_item/', views.add_item, name='add_item'),
    path('item_added/', views.item_added, name='item_added'),
]
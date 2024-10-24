from django.urls import path
from crudapp import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('new/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_update, name='item_update'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dds_list, name='dds_list'),
    path('create/', views.dds_create, name='dds_create'),
    path('edit/<int:pk>/', views.dds_edit, name='dds_edit'),
    path('delete/<int:pk>/', views.dds_delete, name='dds_delete'),

]
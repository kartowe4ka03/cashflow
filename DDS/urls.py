from django.urls import path
from . import views

urlpatterns = [
    path('', views.dds_list, name='dds_list'),
]
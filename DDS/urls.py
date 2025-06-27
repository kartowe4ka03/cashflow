from django.urls import path
from . import views


urlpatterns = [
    path('', views.dds_list, name='dds_list'),
    path('create/', views.dds_create, name='dds_create'),
    path('edit/<int:pk>/', views.dds_edit, name='dds_edit'),
    path('delete/<int:pk>/', views.dds_delete, name='dds_delete'),
    path('refs/type/', views.TypeListView.as_view(), name='ref_type_list'),
    path('refs/type/create/', views.TypeCreateView.as_view(), name='ref_type_create'),
    path('refs/type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='ref_type_edit'),
    path('refs/type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='ref_type_delete'),
    path('refs/status/', views.StatusListView.as_view(), name='ref_status_list'),
    path('refs/status/create/', views.StatusCreateView.as_view(), name='ref_status_create'),
    path('refs/status/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='ref_status_edit'),
    path('refs/status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='ref_status_delete'),
    path('refs/category/', views.CategoryListView.as_view(), name='ref_category_list'),
    path('refs/category/create/', views.CategoryCreateView.as_view(), name='ref_category_create'),
    path('refs/category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='ref_category_edit'),
    path('refs/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='ref_category_delete'),
    path('refs/subcategory/', views.SubCategoryListView.as_view(), name='ref_subcategory_list'),
    path('refs/subcategory/create/', views.SubCategoryCreateView.as_view(), name='ref_subcategory_create'),
    path('refs/subcategory/<int:pk>/edit/', views.SubCategoryUpdateView.as_view(), name='ref_subcategory_edit'),
    path('refs/subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='ref_subcategory_delete'),
]
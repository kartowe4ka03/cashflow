from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------
    # Основной функционал ДДС
    # -------------------------------

    path('', views.dds_list, name='dds_list'),
    # Главная страница со списком записей и фильтрацией

    path('create/', views.dds_create, name='dds_create'),
    # Создание новой записи ДДС

    path('edit/<int:pk>/', views.dds_edit, name='dds_edit'),
    # Редактирование записи по ID

    path('delete/<int:pk>/', views.dds_delete, name='dds_delete'),
    # Удаление записи по ID с подтверждением

    # -------------------------------
    # Центр управления справочниками
    # -------------------------------

    path('refs/', views.RefsHomeView.as_view(), name='refs_home'),
    # Главная страница справочников (выбор раздела)

    # -------------------------------
    # Справочник: Типы
    # -------------------------------

    path('refs/type/', views.TypeListView.as_view(), name='ref_type_list'),
    # Список типов

    path('refs/type/create/', views.TypeCreateView.as_view(), name='ref_type_create'),
    # Создание нового типа

    path('refs/type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='ref_type_edit'),
    # Редактирование типа по ID

    path('refs/type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='ref_type_delete'),
    # Удаление типа по ID

    # -------------------------------
    # Справочник: Статусы
    # -------------------------------

    path('refs/status/', views.StatusListView.as_view(), name='ref_status_list'),
    path('refs/status/create/', views.StatusCreateView.as_view(), name='ref_status_create'),
    path('refs/status/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='ref_status_edit'),
    path('refs/status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='ref_status_delete'),

    # -------------------------------
    # Справочник: Категории
    # -------------------------------

    path('refs/category/', views.CategoryListView.as_view(), name='ref_category_list'),
    path('refs/category/create/', views.CategoryCreateView.as_view(), name='ref_category_create'),
    path('refs/category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='ref_category_edit'),
    path('refs/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='ref_category_delete'),

    # -------------------------------
    # Справочник: Подкатегории
    # -------------------------------

    path('refs/subcategory/', views.SubCategoryListView.as_view(), name='ref_subcategory_list'),
    path('refs/subcategory/create/', views.SubCategoryCreateView.as_view(), name='ref_subcategory_create'),
    path('refs/subcategory/<int:pk>/edit/', views.SubCategoryUpdateView.as_view(), name='ref_subcategory_edit'),
    path('refs/subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='ref_subcategory_delete'),
]

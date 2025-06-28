from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy

from .models import DDSRecord, Status, Type, Category, SubCategory
from .forms import (
    DDSRecordForm, TypeForm, StatusForm, CategoryForm, SubCategoryForm
)

# -----------------------------
# Основные представления ДДС
# -----------------------------

def dds_create(request):
    """
    Представление для создания новой записи ДДС.
    Отображает форму и сохраняет запись при успешной валидации.
    """
    if request.method == 'POST':
        form = DDSRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds_list')
    else:
        form = DDSRecordForm()

    return render(request, 'dds/dds_form.html', {'form': form})


def dds_list(request):
    """
    Главная страница со списком записей ДДС.
    Поддерживает фильтрацию по дате, статусу, типу, категории и подкатегории.
    """
    records = DDSRecord.objects.all().select_related(
        'type', 'status', 'category', 'subcategory'
    )

    # Получение параметров фильтрации из GET-запроса
    type_id = request.GET.get('type')
    status_id = request.GET.get('status')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # Применение фильтров
    if type_id:
        records = records.filter(type_id=type_id)
    if status_id:
        records = records.filter(status_id=status_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)
    if date_from:
        records = records.filter(created_at__gte=date_from)
    if date_to:
        records = records.filter(created_at__lte=date_to)

    context = {
        'records': records,
        'types': Type.objects.all(),
        'statuses': Status.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
        'filters': {
            'type': type_id,
            'status': status_id,
            'category': category_id,
            'subcategory': subcategory_id,
            'date_from': date_from,
            'date_to': date_to,
        }
    }
    return render(request, 'dds/dds_list.html', context)


def dds_edit(request, pk):
    """
    Редактирование существующей записи ДДС.
    """
    record = get_object_or_404(DDSRecord, pk=pk)
    if request.method == 'POST':
        form = DDSRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dds_list')
    else:
        form = DDSRecordForm(instance=record)
    return render(request, 'dds/dds_form.html', {'form': form, 'edit': True})


def dds_delete(request, pk):
    """
    Удаление записи ДДС с подтверждением.
    """
    record = get_object_or_404(DDSRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('dds_list')
    return render(request, 'dds/dds_confirm_delete.html', {'record': record})


# -----------------------------
# Представления справочников
# -----------------------------

# ——— Типы ———

class TypeListView(ListView):
    """Список типов операций."""
    model = Type
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Типы', 'model_name': 'type'}


class TypeCreateView(CreateView):
    """Создание нового типа."""
    model = Type
    form_class = TypeForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_type_list')


class TypeUpdateView(UpdateView):
    """Редактирование типа."""
    model = Type
    form_class = TypeForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_type_list')


class TypeDeleteView(DeleteView):
    """Удаление типа."""
    model = Type
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_type_list')


# ——— Статусы ———

class StatusListView(ListView):
    """Список статусов операций."""
    model = Status
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Статусы', 'model_name': 'status'}


class StatusCreateView(CreateView):
    """Создание нового статуса."""
    model = Status
    form_class = StatusForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_status_list')


class StatusUpdateView(UpdateView):
    """Редактирование статуса."""
    model = Status
    form_class = StatusForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_status_list')


class StatusDeleteView(DeleteView):
    """Удаление статуса."""
    model = Status
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_status_list')


# ——— Категории ———

class CategoryListView(ListView):
    """Список категорий."""
    model = Category
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Категории', 'model_name': 'category'}


class CategoryCreateView(CreateView):
    """Создание новой категории."""
    model = Category
    form_class = CategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_category_list')


class CategoryUpdateView(UpdateView):
    """Редактирование категории."""
    model = Category
    form_class = CategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_category_list')


class CategoryDeleteView(DeleteView):
    """Удаление категории."""
    model = Category
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_category_list')


# ——— Подкатегории ———

class SubCategoryListView(ListView):
    """Список подкатегорий."""
    model = SubCategory
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Подкатегории', 'model_name': 'subcategory'}


class SubCategoryCreateView(CreateView):
    """Создание новой подкатегории."""
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_subcategory_list')


class SubCategoryUpdateView(UpdateView):
    """Редактирование подкатегории."""
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_subcategory_list')


class SubCategoryDeleteView(DeleteView):
    """Удаление подкатегории."""
    model = SubCategory
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_subcategory_list')


# -----------------------------
# Стартовая страница справочников
# -----------------------------

class RefsHomeView(TemplateView):
    """Главная страница для выбора справочников."""
    template_name = 'dds/refs_home.html'
from django.shortcuts import render
from .models import DDSRecord, Status, Type, Category, SubCategory
from.forms import TypeForm, StatusForm, CategoryForm, SubCategoryForm
from .forms import DDSRecordForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy


def dds_create(request):
    if request.method == 'POST':
        form = DDSRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds_list')
    else:
        form = DDSRecordForm()

    return render(request, 'dds/dds_form.html', {'form': form})


def dds_list(request):
    records = DDSRecord.objects.all().select_related(
        'type', 'status', 'category', 'subcategory'
    )

    # Фильтрация
    type_id = request.GET.get('type')
    status_id = request.GET.get('status')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

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
    record = get_object_or_404(DDSRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('dds_list')
    return render(request, 'dds/dds_confirm_delete.html', {'record': record})

# Представления для справочников
# Тип
class TypeListView(ListView):
    model = Type
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Типы', 'model_name': 'type'}


class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_type_create')


class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_type_edit')


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_type_delete')


# Статус
class StatusListView(ListView):
    model = Status
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Статус', 'model_name': 'status'}


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_status_create')


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_status_edit')


class StatusDeleteView(DeleteView):
    model = StatusForm
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_status_delete')


# Категория
class CategoryListView(ListView):
    model = Category
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Категория', 'model_name': 'category'}


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_category_create')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_category_edit')


class CategoryDeleteView(DeleteView):
    model = CategoryForm
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_category_delete')


# Подкатегория
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'dds/ref_list.html'
    context_object_name = 'objects'
    extra_context = {'title': 'Подкатегория', 'model_name': 'subcategory'}


class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_subcategory_create')


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/ref_form.html'
    success_url = reverse_lazy('ref_subcategory_edit')


class SubCategoryDeleteView(DeleteView):
    model = SubCategoryForm
    template_name = 'dds/ref_confirm_delete.html'
    success_url = reverse_lazy('ref_subcategory_delete')


# Домашняя страница для полей формы
class RefsHomeView(TemplateView):
    template_name = 'dds/refs_home.html'
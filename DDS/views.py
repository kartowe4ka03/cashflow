from django.shortcuts import render
from .models import DDSRecord, Status, Type, Category, SubCategory
from django.db.models import Q
from datetime import datetime


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

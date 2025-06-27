from django.contrib import admin
from .models import Type, Status, Category, SubCategory, DDSRecord


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(DDSRecord)
class DDSRecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'type', 'category', 'subcategory', 'status', 'amount']
    list_filter = ['type', 'category', 'subcategory', 'status', 'created_at']
    search_fields = ['comment']
    date_hierarchy = 'created_at'

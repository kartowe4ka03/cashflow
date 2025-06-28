from django import forms
from .models import DDSRecord, Category, SubCategory, Type, Status


class DDSRecordForm(forms.ModelForm):
    """
    Форма создания/редактирования записи ДДС.

    Особенности:
    - Автоматически фильтрует и валидирует поля.
    - Добавляет Bootstrap-классы к полям.
    - Подсвечивает ошибки через is-invalid.
    """
    class Meta:
        model = DDSRecord
        fields = [
            'created_at', 'status', 'type', 'category',
            'subcategory', 'amount', 'comment'
        ]
        widgets = {
            'created_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': 1
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Переопределённый конструктор:
        - Применяет стили Bootstrap (form-control / form-select)
        - Добавляет класс is-invalid к ошибочным полям
        """
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css_class = 'form-control'
            if self.errors.get(name):
                css_class += ' is-invalid'

            # Для полей типа Select используем класс form-select
            if isinstance(field.widget, forms.Select):
                css_class = css_class.replace('form-control', 'form-select')

            field.widget.attrs.update({'class': css_class})


class TypeForm(forms.ModelForm):
    """
    Форма создания/редактирования типа операции.
    """
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class StatusForm(forms.ModelForm):
    """
    Форма создания/редактирования статуса операции.
    """
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    """
    Форма создания/редактирования категории.

    Связана с моделью Type.
    """
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }


class SubCategoryForm(forms.ModelForm):
    """
    Форма создания/редактирования подкатегории.

    Связана с моделью Category.
    """
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

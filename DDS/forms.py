from django import forms
from .models import DDSRecord, Category, SubCategory


class DDSRecordForm(forms.ModelForm):
    class Meta:
        model = DDSRecord
        fields = ['created_at', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].widget.attrs.update({'class': 'form-select'})
        self.fields['type'].widget.attrs.update({'class': 'form-select'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['subcategory'].widget.attrs.update({'class': 'form-select'})

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                cat_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=cat_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()

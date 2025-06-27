from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class DDSRecord(models.Model):
    created_at = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        # Валидация логических связей
        category = getattr(self, 'category', None)
        subcategory = getattr(self, 'subcategory', None)
        type_ = getattr(self, 'type', None)

        if category and type_ and category.type_id != type_.id:
            raise ValidationError("Категория не принадлежит выбранному типу.")

        if subcategory and category and subcategory.category_id != category.id:
            raise ValidationError("Подкатегория не принадлежит выбранной категории.")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.created_at} — {self.type} — {self.amount}₽"

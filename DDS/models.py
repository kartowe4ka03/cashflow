from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Type(models.Model):
    """
    Модель типа операции ДДС (например: Пополнение, Списание).

    Поле:
        name (str): Название типа. Уникальное.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    """
    Модель статуса операции ДДС (например: Бизнес, Личное, Налог).

    Поле:
        name (str): Название статуса. Уникальное.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Категория операции, связанная с определённым типом (Type).

    Примеры:
        Тип: Списание → Категория: Маркетинг

    Поля:
        name (str): Название категории.
        type (Type): Тип операции, к которому принадлежит категория.

    Уникальность:
        Название категории должно быть уникально в рамках одного типа.
    """
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class SubCategory(models.Model):
    """
    Подкатегория операции, связанная с категорией.

    Примеры:
        Категория: Маркетинг → Подкатегория: Avito

    Поля:
        name (str): Название подкатегории.
        category (Category): Родительская категория.

    Уникальность:
        Название подкатегории должно быть уникально в рамках своей категории.
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class DDSRecord(models.Model):
    """
    Основная модель записи движения денежных средств (ДДС).

    Поля:
        created_at (date): Дата создания записи (по умолчанию — сегодня).
        status (Status): Статус записи (например: Бизнес, Личное).
        type (Type): Тип операции (Пополнение или Списание).
        category (Category): Категория, привязанная к типу.
        subcategory (SubCategory): Подкатегория, привязанная к категории.
        amount (Decimal): Сумма операции в рублях.
        comment (str, optional): Необязательный комментарий.

    Логические ограничения:
        - Категория должна принадлежать выбранному типу.
        - Подкатегория должна принадлежать выбранной категории.
    """

    created_at = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        """
        Проверяет логическую корректность связей:
        - категория должна соответствовать типу
        - подкатегория должна соответствовать категории
        """
        category = getattr(self, 'category', None)
        subcategory = getattr(self, 'subcategory', None)
        type_ = getattr(self, 'type', None)

        if category and type_ and category.type_id != type_.id:
            raise ValidationError("Категория не принадлежит выбранному типу.")

        if subcategory and category and subcategory.category_id != category.id:
            raise ValidationError("Подкатегория не принадлежит выбранной категории.")
        
    def save(self, *args, **kwargs):
        """
        Переопределённый save с предварительной валидацией clean().
        """
        self.full_clean()  # вызывает clean() и field-level валидацию
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.created_at} — {self.type} — {self.amount}₽"


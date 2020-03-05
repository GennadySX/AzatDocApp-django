from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название каталога')
    desc = models.TextField(verbose_name='Описание каталога')
    created_at = models.DateField(verbose_name='Дата создания', default=timezone.now)
    updated_at = models.DateField(verbose_name='Дата создания', default=timezone.now)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class Theme(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=350)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = 'Темы'


class Detail(models.Model):
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE)
    detail = models.TextField(verbose_name='Описания темы (текст)')

    class Meta:
        verbose_name = "Описание темы"
        verbose_name_plural = 'Описание темы'

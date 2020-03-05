from django.db import models


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Категории"


class Themes(models.Model):
    category_id = models.OneToOneField(Categories, on_delete= models.CASCADE)
    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=350)

    class Meta:
        verbose_name = "Темы"


class Details(models.Model):
    theme_id = models.OneToOneField( Themes, on_delete= models.CASCADE, primary_key=True)
    detail = models.TextField(verbose_name='Описания темы (текст)')

    class Meta:
        verbose_name = "Описание темы"

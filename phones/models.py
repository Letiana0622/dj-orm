from django.db import models
import datetime
from django.db.models import DateField
from django.urls import reverse

# В файле `models.py` нашего приложения создаем модель Phone с полями
# `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`. Поле `id` - должно быть основным ключом модели.
# * Значение поля `slug` должно устанавливаться слагифицированным значением поля `name`

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    release_date = DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=True)
    pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

# from django.db import models
#
#
# class Car(models.Model):
#     brand = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)
#     color = models.CharField(max_length=20)
# BooleanField
# CharField
# DateField / DateTimeField
# IntegerField
# FloatField
import uuid
from django.db import models

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст заметки")
    date = models.DateTimeField(auto_now=True, editable=False, verbose_name="Дата создания")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    favorite = models.BooleanField(verbose_name="Избранная")

class Category(models.Model):
    name = models.CharField(max_length=88)
    
from django.db import models

# Create your models here.

STATUS_CHOICES = [("new", "New"), ("in_progress", "InProcess"), ("done", "Completed")]


class Article(models.Model):
    project = models.CharField(max_length=250, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    some_date = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def str(self):
        return f"{self.pk}, {self.title}, {self.status}, {self.some_date}"

    class Meta:
        db_table = "article"
        verbose_name = "Задача"
        verbose_name_plural = "Список задач"
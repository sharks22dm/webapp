from django.db import models


# Create your models here.
class MovProduct(models.Model):
    dep_choices = (
        ('Сервис', 'Сервис'),
        ('Молл', 'Молл'),
        ('Плазма', 'Плазма'),
        ('Нагорное', 'Нагорное'),
    )
    status_choices = (
        ('Ожидает сборки', 'Ожидает сборки'),
        ('Собрано', 'Собрано'),
        ('Отменено', 'Отменено'),
    )
    from_dep = models.CharField('Откуда', max_length=10, default='', choices=dep_choices)
    to_dep = models.CharField('Куда', max_length=10, default='', choices=dep_choices)
    product = models.TextField('Наименование товара')
    total = models.IntegerField('Количество', default=1)
    status = models.CharField('Статус товара', max_length=20, choices=status_choices, default='Ожидает сборки')

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return f'/mov_product/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

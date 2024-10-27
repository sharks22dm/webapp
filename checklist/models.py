from django.db import models


class Checklist(models.Model):
    dep_choices = (
        ('Сервис', 'Сервис'),
        ('Молл', 'Молл'),
        ('Плазма', 'Плазма'),
        ('Нагорное', 'Нагорное'),
    )
    title = models.CharField('Название', max_length=30)
    dep = models.CharField('Отдел', max_length=10, choices=dep_choices)
    date = models.DateField('Дата')

    def __str__(self):
        return f'{self.title} - {self.date}'


class Task(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    description = models.CharField('Задание', max_length=500)
    assigned_to = models.CharField('Исполнитель', max_length=20)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.assigned_to} - {self.description}'

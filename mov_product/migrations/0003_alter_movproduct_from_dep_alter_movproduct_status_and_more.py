# Generated by Django 5.1.1 on 2024-10-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov_product', '0002_alter_movproduct_options_movproduct_from_dep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movproduct',
            name='from_dep',
            field=models.CharField(choices=[('Сервис', 'Сервис'), ('Молл', 'Молл'), ('Плазма', 'Плазма'), ('Нагорное', 'Нагорное')], default='', max_length=10, verbose_name='Откуда'),
        ),
        migrations.AlterField(
            model_name='movproduct',
            name='status',
            field=models.CharField(choices=[('Ожидает сборки', 'Ожидает сборки'), ('Собрано', 'Собрано'), ('Отменено', 'Отменено')], default='Ожидает сборки', max_length=20, verbose_name='Статус товара'),
        ),
        migrations.AlterField(
            model_name='movproduct',
            name='to_dep',
            field=models.CharField(choices=[('Сервис', 'Сервис'), ('Молл', 'Молл'), ('Плазма', 'Плазма'), ('Нагорное', 'Нагорное')], default='', max_length=10, verbose_name='Куда'),
        ),
    ]

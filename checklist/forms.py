from django import forms
from django.forms import inlineformset_factory, TextInput, DateInput
from .models import Checklist, Task

dep_choices = [
    ('Сервис', 'Сервис'),
    ('Молл', 'Молл'),
    ('Плазма', 'Плазма'),
    ('Нагорное', 'Нагорное'),
]


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['title', 'dep', 'date']

        widgets = {
            'dep': forms.Select(choices=Checklist.dep_choices, attrs={
                'class': 'form-control'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'assigned_to']

        widgets = {
            'assigned_to': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Исполнитель'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание'
            }),
        }


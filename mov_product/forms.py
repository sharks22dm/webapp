from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class MovProductForm(ModelForm):
    class Meta:
        model = MovProduct
        fields = ['from_dep', 'to_dep', 'product', 'total', 'status']

        widgets = {
            'from_dep': forms.Select(choices=MovProduct.dep_choices, attrs={
                'class': 'form-control'
            }),
            'to_dep': forms.Select(choices=MovProduct.dep_choices, attrs={
                'class': 'form-control'
            }),
            'product': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование товара'
            }),
            'total': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            'status': forms.Select(choices=MovProduct.status_choices, attrs={
                'class': 'form-control',
            }),
        }

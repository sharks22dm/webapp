from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponseRedirect


def mov_product(request):
    return render(request, 'mov_product/mov_product.html')


def check_sale_service(request):
    if request.method == 'POST':
        form = MovProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mov_product/check_sale_service/')
    else:
        form = MovProductForm(initial={
            'status': 'Ожидает сборки'
        })

    return render(request, 'mov_product/check_sale_service.html', {'form': form})


def check_sale_mall(request):
    if request.method == 'POST':
        form = MovProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mov_product/check_sale_mall/')
    else:
        form = MovProductForm(initial={
            'status': 'Ожидает сборки'
        })

    return render(request, 'mov_product/check_sale_mall.html', {'form': form})


def check_sale_plazma(request):
    if request.method == 'POST':
        form = MovProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mov_product/check_sale_plazma/')
    else:
        form = MovProductForm(initial={
            'status': 'Ожидает сборки'
        })

    return render(request, 'mov_product/check_sale_plazma.html', {'form': form})


def check_sale_nagornoe(request):
    if request.method == 'POST':
        form = MovProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mov_product/check_sale_nagornoe/')
    else:
        form = MovProductForm(initial={
            'status': 'Ожидает сборки'
        })

    return render(request, 'mov_product/check_sale_nagornoe.html', {'form': form})


def create_mov_product(request):
    if request.method == 'POST':
        form = MovProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MovProductForm()

    return render(request, 'mov_product/create_mov_product.html', {'form': form})


class MovProductUpdateView(UpdateView):
    model = MovProduct
    success_url = '/mov_product'
    template_name = 'mov_product/create_mov_product.html'
    form_class = MovProductForm


def update_status_sobrano(request, pk):
    product = MovProduct.objects.get(pk=pk)
    product.status = 'Собрано'
    product.save()
    return redirect(request.META.get('HTTP_REFERER'))


def update_status_back(request, pk):
    product = MovProduct.objects.get(pk=pk)
    product.status = 'Ожидает сборки'
    product.save()
    return redirect(request.META.get('HTTP_REFERER'))


def position_delete(request, pk):
    product = MovProduct.objects.get(pk=pk)
    product.delete()
    return JsonResponse({'message': 'Карточка успешно удалена'})


class CustomMovProductListView(ListView):
    model = MovProduct
    context_object_name = 'products'

    def get_template_names(self):
        from_dep = self.kwargs.get('from_dep')
        to_dep = self.kwargs.get('to_dep')
        return f'mov_product/{from_dep.lower()}_to_{to_dep.lower()}.html'

    def get_queryset(self):
        rus_dep = {
            'service': 'Сервис',
            'mall': 'Молл',
            'plazma': 'Плазма',
            'nagornoe': 'Нагорное'
        }
        from_dep = self.kwargs.get('from_dep')
        to_dep = self.kwargs.get('to_dep')
        from_dep_rus = rus_dep.get(from_dep, from_dep)
        to_dep_rus = rus_dep.get(to_dep, to_dep)
        return MovProduct.objects.filter(from_dep=from_dep_rus, to_dep=to_dep_rus)

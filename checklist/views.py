from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import *
from django.views.generic import DetailView
from .models import Checklist


def create_checklist(request, dep):
    """Создание чек-листов для отделов"""
    rus_dep = {
        'service': 'Сервис',
        'mall': 'Молл',
        'plazma': 'Плазма',
        'nagornoe': 'Нагорное'
    }

    if request.method == 'POST':
        form_checklist = ChecklistForm(request.POST)
        if form_checklist.is_valid():
            form_checklist.save()
            return redirect(f'create_checklist_{dep}')
    else:
        rus_dep = rus_dep.get(dep, 'Unknown')
        form_checklist = ChecklistForm(initial={'dep': rus_dep})

    checklists = Checklist.objects.order_by('-date')
    return render(request, f'checklist/create_checklist_{dep}.html',
                  {'form_checklist': form_checklist, 'checklists': checklists})


def create_checklist_service(request):
    return create_checklist(request, 'service')


def create_checklist_mall(request):
    return create_checklist(request, 'mall')


def create_checklist_plazma(request):
    return create_checklist(request, 'plazma')


def create_checklist_nagornoe(request):
    return create_checklist(request, 'nagornoe')


def checklist_update(request, checklist_id):
    """Редактирование задач в чек-листе"""
    checklist = get_object_or_404(Checklist, id=checklist_id)

    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            task = form_task.save(commit=False)
            task.checklist = checklist
            task.save()
            return redirect('checklist_update', checklist_id=checklist_id)
    else:
        form_task = TaskForm()

    tasks = Task.objects.filter(checklist=checklist)
    return render(request, 'checklist/checklist_update.html',
                  {'form_task': form_task, 'tasks': tasks})


def checklist_update_name(request, checklist_id):
    """Редактирование чек-листа"""
    checklist = get_object_or_404(Checklist, id=checklist_id)

    if request.method == 'POST':
        form_checklist = ChecklistForm(request.POST, instance=checklist)
        if form_checklist.is_valid():
            form_checklist.save()
            return redirect('checklist_update', checklist_id=checklist.id)
    else:
        form_checklist = ChecklistForm(instance=checklist)

    return render(request, 'checklist/checklist_update_name.html',
                  {'form_checklist': form_checklist})


def checklist_delete(request, checklist_id):
    """Удаление чек-листа"""
    checklist = get_object_or_404(Checklist, id=checklist_id)
    checklist.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def task_update(request, task_id):
    """Редактирование задачи"""
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form_task = TaskForm(request.POST, instance=task)
        if form_task.is_valid():
            form_task.save()
            return redirect('checklist_update', checklist_id=task.checklist.id)
    else:
        form_task = TaskForm(instance=task)

    return render(request, 'checklist/task_update.html', {'form_task': form_task})


def task_delete(request, task_id):
    """Удаление задачи"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('checklist_update', args=[task.checklist.id]))


class ChecklistView(DetailView):
    """Просмотр задач чек-листа"""
    model = Checklist
    template_name = 'checklist/checklist_view.html'
    context_object_name = 'checklist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checklist = self.get_object()
        tasks = checklist.task_set.all()
        context['tasks'] = tasks
        return context


def task_completed(request, pk):
    """Отметка о выполнении задачи"""
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))


def task_list(request, pk):
    """Возврат о выплнении задачи"""
    task = Task.objects.get(pk=pk)
    task.completed = False
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))

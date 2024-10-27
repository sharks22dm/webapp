from django.urls import path
from . import views

urlpatterns = [
    path('create_checklist_service/', views.create_checklist_service, name='create_checklist_service'),
    path('create_checklist_mall/', views.create_checklist_mall, name='create_checklist_mall'),
    path('create_checklist_plazma/', views.create_checklist_plazma, name='create_checklist_plazma'),
    path('create_checklist_nagornoe/', views.create_checklist_nagornoe, name='create_checklist_nagornoe'),
    path('checklist_update/<int:checklist_id>/', views.checklist_update, name='checklist_update'),
    path('checklist_update_name/<int:checklist_id>/', views.checklist_update_name, name='checklist_update_name'),
    path('checklist/<int:checklist_id>/delete/', views.checklist_delete, name='checklist_delete'),
    path('task_update/<int:task_id>/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/view', views.ChecklistView.as_view(), name='checklist_view'),
    path('<int:pk>/task_completed', views.task_completed, name='task_completed'),
    path('<int:pk>/task_list', views.task_list, name='task_list'),

]

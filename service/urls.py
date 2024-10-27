from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_main, name='service_main')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.nagornoe_main, name='nagornoe_main')
]

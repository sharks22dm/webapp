from django.urls import path
from . import views

urlpatterns = [
    path('', views.plazma_main, name='plazma_main')
]

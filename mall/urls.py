from django.urls import path
from . import views

urlpatterns = [
    path('', views.mall_main, name='mall_main')
]

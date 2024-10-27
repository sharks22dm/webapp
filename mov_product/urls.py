from django.urls import path
from . import views

urlpatterns = [
    path('', views.mov_product, name='mov_product'),
    path('create_mov_product/', views.create_mov_product, name='create_mov_product'),
    path('<int:pk>/update', views.MovProductUpdateView.as_view(), name='position_update'),
    path('<int:pk>/update_status_sobrano', views.update_status_sobrano, name='update_status_sobrano'),
    path('<int:pk>/update_status_back', views.update_status_back, name='update_status_back'),
    path('<int:pk>/position_delete', views.position_delete, name='position_delete'),

    path('<str:from_dep>_to_<str:to_dep>/', views.CustomMovProductListView.as_view(), name='custom_mov_product_list'),

    path('check_sale_service/', views.check_sale_service, name='check_sale_service'),
    path('check_sale_mall/', views.check_sale_mall, name='check_sale_mall'),
    path('check_sale_plazma/', views.check_sale_plazma, name='check_sale_plazma'),
    path('check_sale_nagornoe/', views.check_sale_nagornoe, name='check_sale_nagornoe'),
]

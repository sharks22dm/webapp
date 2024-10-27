from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('service/', include('service.urls')),
    path('mall/', include('mall.urls')),
    path('plazma/', include('plazma.urls')),
    path('nagornoe/', include('nagornoe.urls')),
    path('mov_product/', include('mov_product.urls')),
    path('checklist/', include('checklist.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, include
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
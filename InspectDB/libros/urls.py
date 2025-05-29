from django.urls import path, include
from rest_framework import routers
from .views import AutoresViewSet, LibrosViewSet

router = routers.DefaultRouter()
router.register('autores',AutoresViewSet,'autores')
router.register('libros',LibrosViewSet,'libros')

urlpatterns = [
    path('api/', include(router.urls))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CarViewSet

router = DefaultRouter()
router.register("car", CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, TodoViewSet

router = DefaultRouter()
router.register(r"", TodoViewSet, basename="todo")
router.register(r"categories", CategoryViewSet, basename="category")

# Django tiene la regla que todas las URLs deben crearse en la
# variable urlpatterns
urlpatterns = [
    path("", include(router.urls)),
]

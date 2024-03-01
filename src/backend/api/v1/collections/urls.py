from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.collections.views import CollectionsViewSet

router = DefaultRouter()
router.register(r"collections", CollectionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

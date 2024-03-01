from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.collections.views import (
    CollectionsViewSet,
    PaymentsViewSet,
    ReasonsViewSet,
)

router = DefaultRouter()
router.register(r"collections", CollectionsViewSet, basename="collections")
router.register(r"reasons", ReasonsViewSet)
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

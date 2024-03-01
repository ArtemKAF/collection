from rest_framework.viewsets import ModelViewSet

from api.v1.collections.serializers import (
    CollectionsSerializer,
    PaymentSerializer,
    ReasonSerializer,
)
from apps.collections.models import Collect, Payment, Reason


class ReasonsViewSet(ModelViewSet):
    """Вьюсет целей денежных сборов."""

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class CollectionsViewSet(ModelViewSet):
    """Вьюсет денежных сборов."""

    queryset = Collect.objects.select_related(
        "reason", "author"
    ).prefetch_related("contributors", "payments")

    serializer_class = CollectionsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PaymentsViewSet(ModelViewSet):
    """Вьюсет платежа денежных сборов."""

    queryset = Payment.objects.all().select_related(
        "author",
        "collect__author",
    )
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

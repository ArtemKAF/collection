from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from api.v1.collections.serializers import (
    CollectSerializer,
    PaymentSerializer,
    ReasonSerializer,
)
from api.v1.general.mixins import PerformCreateAuthorMixin
from apps.collections.models import Collect, Payment, Reason

User = get_user_model()


class ReasonsViewSet(ModelViewSet):
    """Вьюсет целей денежных сборов."""

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class CollectionsViewSet(PerformCreateAuthorMixin, ModelViewSet):
    """Вьюсет денежных сборов."""

    queryset = (
        Collect.objects.select_related("reason", "author")
        .only(
            "id",
            "author__last_name",
            "author__first_name",
            "name",
            "reason__name",
            "description",
            "amount",
            "cover",
            "ending",
        )
        .prefetch_related(
            Prefetch("contributors", queryset=User.objects.only("username"))
        )
    )

    serializer_class = CollectSerializer


class PaymentsViewSet(PerformCreateAuthorMixin, ModelViewSet):
    """Вьюсет платежа денежных сборов."""

    queryset = Payment.objects.all().select_related(
        "author",
        "collect__author",
    )
    serializer_class = PaymentSerializer

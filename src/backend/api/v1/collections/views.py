from rest_framework.viewsets import ModelViewSet

from api.v1.collections.serializers import CollectionsSerializer
from apps.collections.models import Collect


class CollectionsViewSet(ModelViewSet):
    """Вьюсет денежных сборов."""

    queryset = Collect.objects.all()
    serializer_class = CollectionsSerializer

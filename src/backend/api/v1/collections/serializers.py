from django.utils.translation import gettext_lazy as _
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.collections.models import Collect


class CollectionsSerializer(serializers.ModelSerializer):
    """Сериализатор денежного сбора."""

    class Meta:
        model = Collect
        fields = "__all__"

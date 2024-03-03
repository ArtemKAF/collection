from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db import models
from drf_extra_fields.fields import Base64ImageField
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from api.v1.collections.constants import ERROR_MESSAGE_UNIQUE_COLLECT
from api.v1.general.mixins import GetAuthorFullNameMixin
from apps.collections.models import Collect, Payment, Reason

User = get_user_model()


class ReasonSerializer(serializers.ModelSerializer):
    """Сериализатор цели денежного сбора."""

    class Meta:
        model = Reason
        fields = "__all__"


class CollectSerializer(GetAuthorFullNameMixin, serializers.ModelSerializer):
    """Сериализатор денежного сбора."""

    author = serializers.SerializerMethodField(read_only=True)
    reason = serializers.SlugRelatedField(
        queryset=Reason.objects.all(),
        slug_field="name",
    )
    cover = Base64ImageField(required=False, allow_null=True)
    contributors_count = serializers.SerializerMethodField(read_only=True)
    collected_amount = serializers.SerializerMethodField(read_only=True)
    contributors = serializers.SlugRelatedField(
        many=True,
        slug_field="username",
        read_only=True,
    )

    class Meta:
        model = Collect
        fields = (
            "id",
            "author",
            "name",
            "reason",
            "description",
            "amount",
            "cover",
            "ending",
            "contributors_count",
            "collected_amount",
            "contributors",
        )

    @extend_schema_field(OpenApiTypes.INT)
    def get_contributors_count(self, obj):
        cache_key = f"collect_contributors_count_{obj.id}"
        contributors_count = cache.get(cache_key)
        if contributors_count is None:
            contributors_count = obj.contributors.only("id").distinct().count()
            cache.set(cache_key, contributors_count)
        return contributors_count

    @extend_schema_field(OpenApiTypes.INT)
    def get_collected_amount(self, obj):
        cache_key = f"collect_collected_amount_{obj.id}"
        collected_amount = cache.get(cache_key)
        if collected_amount is None:
            collected_amount = (
                obj.payments.aggregate(total_amount=models.Sum("amount")).get(
                    "total_amount"
                )
                or 0
            )
            cache.set(cache_key, collected_amount)
        return collected_amount

    def validate(self, attrs):
        """Метод валидации создаваемого денежного сбора."""

        queryset = Collect.objects.filter(
            author=self.context.get("request").user,
            reason=attrs.get("reason"),
            ending__gte=attrs.get("ending"),
        )

        instance = self.instance
        if self.context["request"].method in ["PUT", "PATCH"] and instance:
            queryset = queryset.exclude(id=instance.id)
            if (
                "cover" in attrs
                and attrs["cover"].read() == instance.cover.file.read()
            ):
                attrs.pop("cover")

        if queryset.exists():
            raise serializers.ValidationError(ERROR_MESSAGE_UNIQUE_COLLECT)

        return attrs


class PaymentSerializer(GetAuthorFullNameMixin, serializers.ModelSerializer):
    """Сериализатор денежного платежа."""

    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "author",
            "amount",
            "created",
            "collect",
        )

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property

from apps.collections.constants import (
    MAX_LENGTH_COLLECT_DESCRIPTION,
    MAX_LENGTH_COLLECT_NAME,
    MAX_LENGTH_REASON_NAME,
    UPLOAD_PATH_COLLECT_COVER,
)
from apps.collections.validators import validate_future_datetime
from apps.general.models import CreatedField

User = get_user_model()


class Collect(CreatedField):
    """Модель сбора денежных средств."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        db_index=True,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_COLLECT_NAME,
        null=False,
        blank=False,
    )
    reason = models.ForeignKey(
        "Reason",
        on_delete=models.CASCADE,
        verbose_name="Повод",
        db_index=True,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=MAX_LENGTH_COLLECT_DESCRIPTION,
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма",
        null=True,
        blank=True,
    )
    cover = models.ImageField(
        verbose_name="Обложка",
        upload_to=UPLOAD_PATH_COLLECT_COVER,
        blank=True,
    )
    ending = models.DateTimeField(
        verbose_name="Окончание",
        null=False,
        blank=False,
        validators=[validate_future_datetime],
    )
    contributors = models.ManyToManyField(
        to=User,
        related_name="collect_contributors",
        through="Payment",
        blank=True,
    )

    class Meta:
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"
        default_related_name = "collections"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "author",
                    "reason",
                    "ending",
                ),
                name="%(app_label)s_%(class)s_unique_author_collections",
            ),
        )

    def __str__(self):
        """Метод строкового представления сбора."""

        return self.name

    @cached_property
    def collected_amount(self):
        """Свойство собранных средств на текущий момент."""

        return (
            self.contributors.aggregate(Sum("amount")).get("amount_sum") or 0
        )

    @cached_property
    def contributors_count(self):
        """Свойство количества пожертвовавших."""

        return self.contributors.count()


class Reason(models.Model):
    """Модель цели сбора денежных средств."""

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_REASON_NAME,
        unique=True,
    )

    class Meta:
        verbose_name = "Повод"
        verbose_name_plural = "Поводы"

    def __str__(self):
        """Метод строкового представления повода."""

        return self.name


class Payment(CreatedField):
    """Модель платежа."""

    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        db_index=True,
    )
    collect = models.ForeignKey(
        to=Collect,
        verbose_name="Сбор",
        on_delete=models.CASCADE,
        db_index=True,
    )
    amount = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        default_related_name = "payments"

    def __str__(self):
        """Метод строкового представления платежа."""

        return f"{self.author.username} - {self.amount}"

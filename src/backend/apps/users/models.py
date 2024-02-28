from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.constants import (
    MAX_LENGTH_EMAIL,
    MAX_LENGTH_USERNAME,
    USERNAME_ERROR_TEXT,
    USERNAME_HELP_TEXT,
)


class CustomUserManager(UserManager):
    """Менеджер объектов пользователей."""

    @classmethod
    def normalize_email(cls, email) -> str:
        """Нормализация email. Приведение символов к нижнему регистру."""

        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = f"{email_name.lower()}@{domain_part.lower()}"
        return email


class User(AbstractUser):
    """Модель пользователя."""

    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
        unique=True,
        blank=False,
    )
    username = models.CharField(
        _("username"),
        max_length=MAX_LENGTH_USERNAME,
        unique=True,
        help_text=USERNAME_HELP_TEXT,
        error_messages={
            "unique": USERNAME_ERROR_TEXT,
        },
        validators=[UnicodeUsernameValidator()],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("username",)
        ordering = ("username",)

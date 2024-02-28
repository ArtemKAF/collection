from djoser.serializers import (
    UserCreatePasswordRetypeSerializer,
    UserSerializer,
)

from api.v1.users.constants import ORDERED_USERS_FIELDS


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователя."""

    class Meta(UserSerializer.Meta):
        fields = ORDERED_USERS_FIELDS


class CustomUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Сериализатор для регистрации пользователя с подтверждением пароля."""

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = ORDERED_USERS_FIELDS + ("password",)

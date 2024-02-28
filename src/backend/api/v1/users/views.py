from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from apps.users.models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет пользователя."""

    queryset = get_user_model().objects.all()

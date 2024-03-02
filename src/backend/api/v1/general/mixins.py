from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class PerformCreateAuthorMixin:
    """
    Миксин сохранения объекта с пользователем из запроса в качестве автора.
    """

    def perform_create(self, serializer):
        """Метод предварительного создания объекта."""

        serializer.save(author=self.request.user)


class GetAuthorFullNameMixin:
    """
    Миксин сохранения объекта с пользователем из запроса в качестве автора.
    """

    @extend_schema_field(OpenApiTypes.STR)
    def get_author(self, obj):
        """Метод получения полного имени у автора объекта."""

        return obj.author.get_full_name()

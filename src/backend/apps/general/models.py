from django.db import models


class CreatedField(models.Model):
    """
    Абстрактная модель с полем для сохранения даты и времени создания объекта.
    """

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ModifiedField(models.Model):
    """
    Абстрактная модель с полем для сохранения даты и времени изменения объекта.
    """

    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

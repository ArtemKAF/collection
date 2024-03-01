from django.core.validators import ValidationError
from django.utils import timezone


def validate_future_datetime(value):
    """Метод проверки, что значение не меньше текушей даты и времени."""

    if value < timezone.now():
        raise ValidationError("Нельзя указать прошедшую дату и время.")

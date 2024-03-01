import json
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.collections.models import Collect, Payment, Reason

User = get_user_model()

FILES_DICT = {
    User: "users.json",
    Reason: "reasons.json",
    Collect: "collections.json",
    Payment: "payments.json",
}


class Command(BaseCommand):
    """Команда для загрузки предварительных данных из csv файлов в БД."""

    help = "Загрузка предварительных данных из csv файлов."

    def handle(self, *args, **kwargs):
        """Обработчик мэнэджмент команды."""

        for model, file_name in FILES_DICT.items():
            try:
                file_path = os.path.join(os.getcwd(), "data", file_name)
                with open(file_path) as json_file:
                    data = json.load(json_file)
                    model.objects.bulk_create(model(**entry) for entry in data)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Модель - {model.__name__} - загрузка успешна."
                    )
                )
            except Exception as error:
                self.stdout.write(
                    self.style.ERROR(f"{error} for model {model.__name__}")
                )
        self.stdout.write(self.style.SUCCESS("Процесс загрузки завершен."))

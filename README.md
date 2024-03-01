# collection backend
RESTfull API приложение, разработанное в рамках тестового задания для организации
групповых денежных сборов.

[![Code cheсks](https://github.com/ArtemKAF/collection/actions/workflows/code_check.yml/badge.svg)](https://github.com/ArtemKAF/collection/actions/workflows/code_check.yml/badge.svg)

## Стек технологий:

[![Python][Python-badge]][Python-url]
[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![Postgres][Postgres-badge]][Postgres-url]
[![Nginx][Nginx-badge]][Nginx-url]

## Требования

1. **Python 3.12**  

2. **Poetry**  
   Зависимости и пакеты управляются через [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
   ```
   poetry install --no-root
   ```
    [документация](https://python-poetry.org/docs/basic-usage/).  

3. **Docker Compose**  
    Для запуска проекта в докер контейнерах.

### Как запустить проект локально:
- Клонировать репозиторий
- Активировать виртуальное окружение командой
```
poetry shell
```
- Установить зависимости командой
```
poetry install --no-root
```
- В корневой директории проекта подготовить файл .env и наполнить по шаблону из .env.example
- В терминале из директории src/backend выполнить команду
```
python manage.py runserver --settings config.settings.local
```
По завершении работы команды проект станет доступен по адресу [http://localhost:8000/](http://localhost:8000/) или [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

По адресу [http://localhost:8000/api/v1/schema/docs/](http://localhost:8000/api/v1/schema/docs/) будет доступна спецификация к API проекта.

### Как запустить проект локально в докер контейнерах:
- В корневой директории проекта подготовить файл .env и наполнить по шаблону из .env.example
- В терминале из директории infra выполнить команду
```
sudo docker compose up -d
```
По завершении работы команды проект станет доступен по адресу [http://localhost/](http://localhost/) или [http://127.0.0.1/](http://127.0.0.1/)  

По адресу [http://localhost/api/v1/schema/docs/](http://localhost/api/v1/schema/docs/) будет доступна спецификация к API проекта.

<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/

[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Django-url]: https://github.com/django/django

[Django-badge]: https://img.shields.io/badge/Django-0c4b33?style=for-the-badge&logo=django&logoColor=white

[DRF-url]: https://github.com/encode/django-rest-framework

[DRF-badge]: https://img.shields.io/badge/DRF-A30000?style=for-the-badge

[Postgres-url]: https://www.postgresql.org/

[Postgres-badge]: https://img.shields.io/badge/postgres-306189?style=for-the-badge&logo=postgresql&logoColor=white

[Nginx-url]: https://nginx.org

[Nginx-badge]: https://img.shields.io/badge/nginx-009900?style=for-the-badge&logo=nginx&logoColor=white

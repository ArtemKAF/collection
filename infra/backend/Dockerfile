FROM python:3.12.0-alpine3.18

WORKDIR /app
COPY infra/backend/requirements/prod.txt /app/requirements.txt

RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY src/backend/. /app/
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]

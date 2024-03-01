from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = getenv("SECRET_KEY", default="insecure")


DEBUG = getenv("DEBUG", default="False") == "True"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "drf_spectacular",
]

LOCAL_APPS = [
    "apps.general",
    "apps.users",
    "apps.collections",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": getenv("POSTGRES_DB", default="collection_db"),
        "USER": getenv("POSTGRES_USER", default="collection_user"),
        "PASSWORD": getenv("POSTGRES_PASSWORD", default="collection_pass"),
        "HOST": getenv("POSTGRES_HOST", default="db"),
        "PORT": getenv("POSTGRES_PORT", default=5432),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = Path(BASE_DIR, "collected_static")

MEDIA_URL = "media/"
MEDIA_ROOT = Path(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "HIDE_USERS": False,
    "PERMISSIONS": {
        "user_list": ["rest_framework.permissions.IsAuthenticated"],
    },
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SERIALIZERS": {
        "current_user": "api.v1.users.serializers.CustomUserSerializer",
        "user": "api.v1.users.serializers.CustomUserSerializer",
        "user_create_password_retype": "api.v1.users.serializers.CustomUserCreateSerializer",
    },
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "#/login/{uid}/{token}",
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Collection",
    "DESCRIPTION": "Collection - приложение для организации групповых денежных сборов.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "filter": True,
    },
    "COMPONENT_SPLIT_REQUEST": True,
}

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

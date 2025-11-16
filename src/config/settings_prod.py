import os

from celery.schedules import crontab

from .settings import *  # noqa: F403

DEBUG = int(os.environ.get("DEBUG", default=0))

CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.contrib.gis.db.backends.postgis"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get(
            "DB_HOST",
        ),
        "PORT": os.environ.get("DB_PORT"),
    }
}

CELERY_BEAT_SCHEDULE = {
    "purge-soft-deleted-users": {
        "task": "apps.accounts.tasks.delete_expired_users",
        "schedule": crontab(minute="*/5"),
        # "schedule": crontab(hour=0, minute=0, day_of_week="mon"),
    }
}

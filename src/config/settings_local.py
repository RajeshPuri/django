import os

from .settings import *  # noqa: F403

DEBUG = int(os.environ.get("DEBUG", default=1))
# DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get(
            "DB_HOST",
        ),
        "PORT": os.environ.get("DB_PORT"),
    }
}

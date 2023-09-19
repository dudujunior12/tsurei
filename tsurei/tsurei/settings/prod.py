from .base import *

import dj_database_url

# Application definition

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "manga",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
    }
}

DATABASES["default"] = dj_database_url.config(default=env("POSTGRES_URL"))

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

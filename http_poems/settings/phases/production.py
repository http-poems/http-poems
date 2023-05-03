from decouple import Csv

from http_poems.settings.default import *  # NoQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
    },
}

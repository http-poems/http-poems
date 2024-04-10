from decouple import Csv

from http_poems.settings.default import *  # NoQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

from http_poems.settings.default import *  # NoQA

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", True, cast=bool)

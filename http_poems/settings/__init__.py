from decouple import config

PHASE = config("PHASE", "local")

match PHASE:
    case "development":
        from http_poems.settings.phases.development import *  # NOQA
    case "production":
        from http_poems.settings.phases.production import *  # NOQA
    case _:
        raise Exception("PHASE environment variable not set probably.")

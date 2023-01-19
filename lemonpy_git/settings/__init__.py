from decouple import config


if config("SETTINGS-DEV-OR-PROD") == "prod":
    from .prod import *
else:
    from .dev import *
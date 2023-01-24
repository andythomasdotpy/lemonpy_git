import os
from decouple import config


# SETTINGS_PROD = "prod"

# os.environ.get('TWITTER_ACCESS_TOKEN')
try:
    print(f"printing **before** {config('SETTINGS_PATH')}")

    if config('SETTINGS_PATH') == "prod":
        print("prod.py settings activated!")
        from .prod import *
except:
    print("SETTINGS_PATH not equal to prod..")
    print("dev.py settings activated!")
    from .dev import *
from decouple import config, Csv

from .base import *

print("prod")

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
# ALLOWED_HOSTS = [
#     "lemonpy.com",
#     "www.lemonpy.com"
# ]

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "staticfiles"),
   ]

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
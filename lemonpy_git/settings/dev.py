from decouple import config

from .base import *


print("dev")
SECRET_KEY = config("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
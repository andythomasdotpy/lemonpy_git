from decouple import config

from .base import *

print("dev")

SECRET_KEY = config("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []
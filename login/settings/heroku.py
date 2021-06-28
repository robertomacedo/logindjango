import environ


from login.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRETY_KEY')

ALLOWED_HOSTS = list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}
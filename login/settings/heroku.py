import environ


from login.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

<<<<<<< HEAD
SECRET_KEY = env('SECRETY_KEY')
=======
SECRET_KEY = env('SECRET_KEY')
>>>>>>> d3e761c1907f82a852afc57ee51713c56c5327a9

ALLOWED_HOSTS = list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}
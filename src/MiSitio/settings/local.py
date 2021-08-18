
from .base import *


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prestamos',
        'USER': 'postgres',
        'PASSWORD': '3624365017rataricsofia',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
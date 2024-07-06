from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': config('DATABASE_HOST'),
        'NAME': config('DATABASE_DB'),
        'PORT': config('DATABASE_PORT'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'options': '-c timezone=Asia/Tashkent',
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True

SERVER_IP = config('SERVER_IP', default='')
SERVER_DOMAIN = config('SERVER_DOMAIN', default='')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = [SERVER_IP, SERVER_DOMAIN]

CSRF_TRUSTED_ORIGINS = [
    f'https://{SERVER_DOMAIN}',
    f'http://{SERVER_DOMAIN}',
]

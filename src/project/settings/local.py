from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'backend.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': config('POSTGRES_HOST'),
        'NAME': config('POSTGRES_DB'),
        'PORT': config('POSTGRES_PORT'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'options': '-c timezone=Asia/Tashkent',
        },
    },
}

ALLOWED_HOSTS = ['*']

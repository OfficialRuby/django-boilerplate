from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

    }
}

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

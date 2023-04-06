from django.core.management.utils import get_random_secret_key
from .base import *
from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


sentry_sdk.init(
    dsn=config('SENTRY_DNS'),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=0.1,
    send_default_pii=True
)

# HTTPS
# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True
# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True
# The lifetime of a database connection, as an integer of seconds.
CONN_MAX_AGE = 600
# Without this, your site cannot be submitted to the browser preload list
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_HTTPONLY = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

from .base import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': Secret.DATABASES['default']['ENGINE'],
        'NAME': Secret.DATABASES['default']['NAME'],
        'USER': Secret.DATABASES['default']['USER'],
        'PASSWORD': Secret.DATABASES['default']['PASSWORD'],
        'HOST': Secret.DATABASES['default']['HOST'],
        'PORT': Secret.DATABASES['default']['PORT'],
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

# Media files (Upload)
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/path/to/logs/django.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

INSTALLED_APPS += []

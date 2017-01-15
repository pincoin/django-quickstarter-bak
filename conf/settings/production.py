from .base import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config['LOCAL']['DATABASE_ENGINE'],
        'NAME': config['LOCAL']['DATABASE_NAME'],
        'USER': config['LOCAL']['DATABASE_USER'],
        'PASSWORD': config['LOCAL']['DATABASE_PASSWORD'],
        'HOST': config['LOCAL']['DATABASE_HOST'],
        'PORT': config['LOCAL']['DATABASE_PORT'],
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media files (Upload)
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += []

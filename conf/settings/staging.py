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

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

# Media files (Upload)
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

INSTALLED_APPS += []

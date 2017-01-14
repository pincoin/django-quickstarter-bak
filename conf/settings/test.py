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

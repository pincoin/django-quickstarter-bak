import os

try:
    from .secret import *
except ImportError:
    raise ImportError(
        "Couldn't import Secret values. Are you sure secret.py exists and "
        "available on conf.settings package?"
    )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
DEBUG = Secret.DEBUG
ALLOWED_HOSTS = Secret.ALLOWED_HOSTS
SECRET_KEY = Secret.SECRET_KEY
DATABASES = Secret.DATABASES

# Application definition
INSTALLED_APPS = [
    # 'account_old.apps.AccountConfig',  # Must precede 'django.contrib.admin' and 'django.contrib.auth'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Email settings
# https://docs.djangoproject.com/en/1.11/topics/email/
EMAIL_BACKEND = Secret.EMAIL_BACKEND
EMAIL_HOST = Secret.EMAIL_HOST
EMAIL_PORT = Secret.EMAIL_PORT
EMAIL_HOST_USER = Secret.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = Secret.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = Secret.EMAIL_USE_TLS

SITE_ID = 1

# Authentication settings
# Custom auth user model
# AUTH_USER_MODEL = 'account_old.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default model backend
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django.contrib.auth
PASSWORD_RESET_TIMEOUT_DAYS = 1  # default=3
LOGIN_URL = '/accounts/login/'  # default=/accounts/login/
LOGOUT_URL = '/accounts/logout/'  # default=/accounts/logout/
LOGIN_REDIRECT_URL = '/'  # default=/accounts/profile/
# LOGOUT_REDIRECT_URL = '/'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

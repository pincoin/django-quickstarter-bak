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
    'account.apps.AccountConfig',  # Must precede 'django.contrib.admin' and 'django.contrib.auth'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
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

# Authentication settings
# Authentication backends with SNS
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.line.LineOAuth2',
    'social_core.backends.kakao.KakaoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Custom auth user model
AUTH_USER_MODEL = 'account.User'
AUTH_USERNAME_FIELD = 'email'
AUTH_REQUIRED_FIELDS = ['username', 'last_name', 'first_name', ]

# django.contrib.auth
LOGIN_URL = '/accounts/login/'  # default=/accounts/login/
LOGOUT_URL = '/accounts/logout/'  # default=/accounts/logout/
LOGIN_REDIRECT_URL = '/'  # default=/accounts/profile/
# LOGOUT_REDIRECT_URL = '/'

# django-registration
REGISTRATION_OPEN = True  # default=True
ACCOUNT_ACTIVATION_DAYS = 1  # Enables 2-phase registration
PASSWORD_RESET_TIMEOUT_DAYS = 1  # default=3

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# OAuth
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # 'social_core.pipeline.mail.mail_validation',
    # 'social_core.pipeline.social_auth.associate_by_email',
    # 'social_core.pipeline.user.create_user',
    'account.social.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SOCIAL_AUTH_FACEBOOK_KEY = Secret.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = Secret.SOCIAL_AUTH_FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # Fetch email address
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, last_name, first_name',
}

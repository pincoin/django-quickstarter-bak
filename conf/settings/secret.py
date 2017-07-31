class Secret:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # SECURITY WARNING: declare allowed hosts explicitly in production!
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', ]

    # SECURITY WARNING: keep the secret key used in production secret!
    # http://www.miniwebtool.com/django-secret-key-generator/
    SECRET_KEY = 'whn$t)md9-o^fo6=b_u%+03yvpn_&yio#+!qc@n&uwajk1zr=%'

    # Database (default: SQLite3)
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
            'USER': None,
            'PASSWORD': None,
            'HOST': None,
            'PORT': None,
        }
    }

    # Email settings
    # App password is required for Gmail.
    # https://security.google.com/settings/security/apppasswords
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'pincoins@gmail.com'
    EMAIL_HOST_PASSWORD = 'angtkhbatjymeuhe'
    EMAIL_USE_TLS = True

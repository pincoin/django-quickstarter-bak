class Secret:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', ]

    # SECRET KEY GENERATOR: KEEP THIS VALUE SECRET.
    # http://www.miniwebtool.com/django-secret-key-generator/
    SECRET_KEY = 'ae87@-b^6m9fw=gsu@=+7bv&&kpdt^$ay7ztikwjnz_w6$i@6p'

    # SQLite3
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

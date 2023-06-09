from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1','cnsapp','www.cnsapp','10.0.0.182']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

SECRET_KEY = get_secret('DJANGO_SECRET_KEY')
DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': get_secret("DATABASE_NAME"),
           'USER': get_secret("DATABASE_USER"),
           'PASSWORD': get_secret("DATABASE_PASSWORD"),
           'HOST':get_secret("DATABASE_HOST"),
           'PORT':get_secret("DATABASE_PORT")
    },
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME':"postgres",
    #         'USER': "postgres",
    #         'PASSWORD': "ANALISISUASD",
    #         'HOST':"10.0.0.182",
    #         'PORT':"5432"
    # },
    #  'default': {
    #      'ENGINE': 'django.db.backends.sqlite3',
    #      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #  }
}
# print(SECRET_KEY)
# import dj_database_url  
# db_from_env = dj_database_url.config(conn_max_age=500)  
# DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}
# Activate Django-Heroku.
# django_heroku.settings(locals())
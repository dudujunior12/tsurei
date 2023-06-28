from .base import *

import dj_database_url
#import cloudinary
#import cloudinary.uploader
#import cloudinary.api

# Application definition

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

INSTALLED_APPS = [
    #'whitenoise.runserver_nostatic',
    'manga',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

DATABASES['default'] = dj_database_url.config(default=env("POSTGRES_URL"))

#CLOUDINARY_STORAGE = {
#    'CLOUD_NAME': env('CLOUD_NAME'),
#    'API_KEY': env("API_KEY"),
#    'API_SECRET': env('API_SECRET'),
#}

#DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
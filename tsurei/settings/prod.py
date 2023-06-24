from .base import *

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Application definition

INSTALLED_APPS = [
    'manga',
    'cloudinary',
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


#The absolute path where collectstatic will collect all static files
STATICFILES_DIRS = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env("API_KEY"),
    'API_SECRET': env('API_SECRET'),
}

DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")
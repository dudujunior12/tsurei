from .base import *

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

DATABASES['default'] = dj_database_url.config(default=env("POSTGRES_URL"))

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env("API_KEY"),
    'API_SECRET': env('API_SECRET'),
}

DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")
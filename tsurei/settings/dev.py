from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
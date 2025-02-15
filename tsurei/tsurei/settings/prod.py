from .base import *

import os

from .base import *

domain = os.getenv("DOMAIN")

STATIC_ROOT = BASE_DIR / "../staticfiles"
ALLOWED_HOSTS = [
    domain,
    f"www.{domain}",
    "localhost",
    "backend",
    "127.0.0.1",
    "0.0.0.0",
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
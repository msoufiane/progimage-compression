"""
ProgImageCompressor base settings to be extended and/or overriden in a local config file.
"""
from ProgImageCompressor.settings.rest_framework.config import REST_FRAMEWORK
from ProgImageCompressor.settings.apps.config import INSTALLED_APPS
from ProgImageCompressor.settings.middleware.config import MIDDLEWARE
from ProgImageCompressor.settings.db.config import DATABASES
from ProgImageCompressor.settings.logging.config import *

import os

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'DEFINE_A_SECURE_KEY')
ROOT_URLCONF = 'ProgImageCompressor.urls'
WSGI_APPLICATION = 'ProgImageCompressor.wsgi.application'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

ALLOWED_HOSTS = [
    ''
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

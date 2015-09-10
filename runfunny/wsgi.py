"""
WSGI config for runfunny project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from os.path import dirname, join

from django.core.wsgi import get_wsgi_application

import dotenv

project_dir = dirname(dirname(__file__))
dotenv.read_dotenv(join(project_dir, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "runfunny.settings")

application = get_wsgi_application()

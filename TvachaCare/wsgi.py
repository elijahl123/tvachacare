"""
WSGI config for TvachaCare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TvachaCare.settings')

application = get_wsgi_application()

sys.path.append('/opt/bitnami/apps/django/django_projects/tvachacare')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/tvachacare/egg_cache")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TvachaCare.settings')

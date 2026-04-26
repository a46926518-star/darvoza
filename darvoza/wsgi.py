"""
WSGI config for darvoza project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'darvoza'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'darvoza.settings')

application = get_wsgi_application()

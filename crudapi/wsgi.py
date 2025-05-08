"""
WSGI config for crudapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from tasks import migrations


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudapi.settings')

application = get_wsgi_application()


from django.core.management import call_command
try:
    call_command('run_migrations')
except Exception as e:
    print(f"Migration failed: {e}")
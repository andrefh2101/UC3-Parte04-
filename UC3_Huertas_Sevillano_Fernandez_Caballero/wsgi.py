"""
WSGI config for UC3_Huertas_Sevillano_Fernandez_Caballero project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UC3_Huertas_Sevillano_Fernandez_Caballero.settings')

application = get_wsgi_application()

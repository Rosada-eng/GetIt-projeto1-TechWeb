"""
WSGI config for getit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'getit.settings')

#! Utilizando outra biblioteca diferente do gunicorn
#! Caso necessário, substitua o código abaixo para application
# # If using WhiteNoise:
# from whitenoise import WhiteNoise
# application = WhiteNoise(get_wsgi_application())

application = get_wsgi_application()
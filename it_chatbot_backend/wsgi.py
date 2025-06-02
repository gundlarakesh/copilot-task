"""
WSGI config for it_chatbot_backend project.

This module contains the WSGI application used by Django's development server and any WSGI-compatible web server.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_chatbot_backend.settings')

application = get_wsgi_application()
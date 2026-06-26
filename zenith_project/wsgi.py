"""
WSGI config for zenith_project project.
This file is used to deploy the application on a web server.
For development, we use 'python manage.py runserver' instead.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zenith_project.settings')
application = get_wsgi_application()

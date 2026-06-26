"""
ZENITH - Main URL Configuration
================================
This file is the entry point for all URLs in the project.
When a user visits a URL, Django checks this file first,
then routes to the correct app.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),         # Django admin panel at /admin/
    path('', include('zenith.urls')),        # All other URLs go to our zenith app
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

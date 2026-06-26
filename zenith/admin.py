"""
ZENITH - Admin Configuration
==============================
This file registers our models with Django's Admin panel.
After registering, you can manage all data through /admin/ URL.

Django Admin is a powerful auto-generated interface for managing database records.
It's great for adding sample data, managing tournaments, etc.
"""

from django.contrib import admin
from .models import Game, FitnessSession, Tournament


# Customize how Game appears in admin panel
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ['title', 'sport', 'location', 'date', 'time', 'players_needed', 'host']
    
    # Filters on the right sidebar
    list_filter = ['sport', 'date']
    
    # Search by these fields
    search_fields = ['title', 'location', 'host__username']
    
    # Order by date
    ordering = ['date']


# Customize how FitnessSession appears in admin panel
@admin.register(FitnessSession)
class FitnessSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'location', 'date', 'time']
    list_filter = ['activity_type', 'date']
    search_fields = ['title', 'location']
    ordering = ['date']


# Customize how Tournament appears in admin panel
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'sport', 'location', 'start_date', 'end_date', 'prize_pool']
    list_filter = ['sport', 'start_date']
    search_fields = ['name', 'location']
    ordering = ['start_date']

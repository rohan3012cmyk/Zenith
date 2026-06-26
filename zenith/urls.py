"""
ZENITH - URL Patterns
======================
This file maps URLs to view functions.
When a user visits /games/, Django looks here, finds it maps to 'games_list' view,
and calls that function.

Format: path('url/', view_function, name='url_name')
The 'name' lets us use {% url 'url_name' %} in templates instead of hardcoding URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Games URLs
    path('games/', views.games_list, name='games_list'),                          # List all games
    path('games/create/', views.create_game, name='create_game'),                 # Create new game
    path('games/my/', views.my_games, name='my_games'),                           # My created games
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),          # View single game
    path('games/<int:game_id>/edit/', views.edit_game, name='edit_game'),         # Edit a game
    path('games/<int:game_id>/delete/', views.delete_game, name='delete_game'),   # Delete a game
    path('games/<int:game_id>/join/', views.join_game, name='join_game'),         # Join a game
    path('games/<int:game_id>/leave/', views.leave_game, name='leave_game'),      # Leave a game

    # Fitness URLs
    path('fitness/', views.fitness_list, name='fitness_list'),

    # Tournament URLs
    path('tournaments/', views.tournament_list, name='tournament_list'),
]

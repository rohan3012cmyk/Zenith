"""
ZENITH - Views
===============
Views are the brain of the application.
Each view function receives an HTTP request and returns an HTTP response.
Views contain all the business logic - what to fetch from DB, what to show the user.

Pattern used: Function-Based Views (FBV)
These are simpler and easier to understand than Class-Based Views,
which is why they're perfect for a college project.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required  # Blocks non-logged-in users
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # For showing success/error alerts
from django.contrib.auth.models import User

from .models import Game, FitnessSession, Tournament
from .forms import RegisterForm, GameForm


# ============================================================
#   HOME PAGE
# ============================================================

def home(request):
    """
    The landing page of ZENITH.
    If user is already logged in, redirect them to dashboard.
    Otherwise, show the home/welcome page.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')  # Already logged in? Go to dashboard
    return render(request, 'zenith/home.html')


# ============================================================
#   AUTHENTICATION VIEWS
# ============================================================

def register_view(request):
    """
    Handles user registration.
    GET request: Show the empty registration form.
    POST request: Validate form data and create user account.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')  # Already logged in, no need to register again

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to database
            login(request, user)  # Automatically log in after registration
            messages.success(request, f'Welcome to ZENITH, {user.username}! Your account has been created.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        # GET request - just show an empty form
        form = RegisterForm()

    return render(request, 'zenith/register.html', {'form': form})


def login_view(request):
    """
    Handles user login.
    GET request: Show the login form.
    POST request: Check credentials and log the user in.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Check username+password
            if user is not None:
                login(request, user)  # Create session - user is now logged in
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'zenith/login.html', {'form': form})


def logout_view(request):
    """
    Logs the user out and redirects to login page.
    @login_required decorator means: if not logged in, redirect to LOGIN_URL.
    """
    logout(request)
    messages.info(request, 'You have been logged out. See you again!')
    return redirect('login')


# ============================================================
#   DASHBOARD VIEW
# ============================================================

@login_required  # User must be logged in to see the dashboard
def dashboard(request):
    """
    Main dashboard shown after login.
    Shows summary counts and recent games.
    """
    # Fetch counts for the stat cards
    total_games = Game.objects.count()
    total_fitness = FitnessSession.objects.count()
    total_tournaments = Tournament.objects.count()

    # Get 3 most recent upcoming games for the preview section
    recent_games = Game.objects.all()[:3]

    context = {
        'total_games': total_games,
        'total_fitness': total_fitness,
        'total_tournaments': total_tournaments,
        'recent_games': recent_games,
        'user': request.user,
    }
    return render(request, 'zenith/dashboard.html', context)


# ============================================================
#   GAMES VIEWS
# ============================================================

@login_required
def games_list(request):
    """
    Shows all available games.
    Also handles search filtering if user types in search box.
    """
    games = Game.objects.all()  # Get all games from DB

    # Search functionality - filter by sport or location
    search_query = request.GET.get('search', '')  # Get search term from URL like ?search=cricket
    sport_filter = request.GET.get('sport', '')   # Get sport filter from URL like ?sport=cricket

    if search_query:
        # Filter games where title or location contains the search query
        games = games.filter(title__icontains=search_query) | games.filter(location__icontains=search_query)

    if sport_filter:
        games = games.filter(sport=sport_filter)

    # Pass all sport choices for the filter dropdown
    sport_choices = Game.SPORT_CHOICES

    context = {
        'games': games,
        'search_query': search_query,
        'sport_filter': sport_filter,
        'sport_choices': sport_choices,
    }
    return render(request, 'zenith/games_list.html', context)


@login_required
def game_detail(request, game_id):
    """
    Shows full details of a single game.
    Also handles the "Join Game" button click.
    
    get_object_or_404: if game with game_id doesn't exist, show 404 error page
    """
    game = get_object_or_404(Game, id=game_id)
    is_host = (request.user == game.host)  # Is the current user the game creator?
    has_joined = game.players.filter(id=request.user.id).exists()  # Has user already joined?

    context = {
        'game': game,
        'is_host': is_host,
        'has_joined': has_joined,
    }
    return render(request, 'zenith/game_detail.html', context)


@login_required
def create_game(request):
    """
    Allows logged-in users to create a new game.
    GET: Show empty create game form.
    POST: Validate and save the new game.
    """
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)  # Don't save to DB yet
            game.host = request.user         # Set the host to current logged-in user
            game.save()                      # Now save to DB
            messages.success(request, f'Game "{game.title}" has been created successfully!')
            return redirect('games_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = GameForm()

    return render(request, 'zenith/create_game.html', {'form': form})


@login_required
def edit_game(request, game_id):
    """
    Allows the game HOST to edit their own game.
    Other users cannot edit games they didn't create.
    """
    game = get_object_or_404(Game, id=game_id)

    # Security check: only the host can edit
    if request.user != game.host:
        messages.error(request, 'You can only edit games that you created.')
        return redirect('games_list')

    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)  # instance=game means we're editing, not creating
        if form.is_valid():
            form.save()
            messages.success(request, f'Game "{game.title}" has been updated.')
            return redirect('games_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = GameForm(instance=game)  # Pre-fill form with existing game data

    return render(request, 'zenith/edit_game.html', {'form': form, 'game': game})


@login_required
def delete_game(request, game_id):
    """
    Allows the game HOST to delete their own game.
    Only processes DELETE on POST request (safety measure).
    """
    game = get_object_or_404(Game, id=game_id)

    # Security check: only the host can delete
    if request.user != game.host:
        messages.error(request, 'You can only delete games that you created.')
        return redirect('games_list')

    if request.method == 'POST':
        game_title = game.title
        game.delete()
        messages.success(request, f'Game "{game_title}" has been deleted.')
        return redirect('games_list')

    # GET request: show confirmation page
    return render(request, 'zenith/delete_game.html', {'game': game})


@login_required
def join_game(request, game_id):
    """
    Handles a user joining a game.
    Checks: user not already joined, game not full, user not the host.
    """
    game = get_object_or_404(Game, id=game_id)

    if request.user == game.host:
        messages.info(request, "You are already the host of this game!")
    elif game.players.filter(id=request.user.id).exists():
        messages.info(request, "You have already joined this game.")
    elif game.is_full():
        messages.warning(request, "Sorry, this game is already full.")
    else:
        game.players.add(request.user)  # Add user to the ManyToMany players field
        messages.success(request, f'You have successfully joined "{game.title}"!')

    return redirect('game_detail', game_id=game_id)


@login_required
def leave_game(request, game_id):
    """
    Handles a user leaving a game they previously joined.
    """
    game = get_object_or_404(Game, id=game_id)

    if game.players.filter(id=request.user.id).exists():
        game.players.remove(request.user)  # Remove from ManyToMany
        messages.success(request, f'You have left "{game.title}".')
    else:
        messages.info(request, "You are not a member of this game.")

    return redirect('games_list')


@login_required
def my_games(request):
    """
    Shows all games the current user has created.
    This is their personal game management page.
    """
    # Filter games where host = current user
    hosted_games = Game.objects.filter(host=request.user)
    # Games the user has joined (not hosted)
    joined_games = request.user.joined_games.all()

    context = {
        'hosted_games': hosted_games,
        'joined_games': joined_games,
    }
    return render(request, 'zenith/my_games.html', context)


# ============================================================
#   FITNESS VIEWS
# ============================================================

@login_required
def fitness_list(request):
    """
    Shows all fitness sessions available.
    """
    sessions = FitnessSession.objects.all()
    
    # Filter by activity type if selected
    activity_filter = request.GET.get('activity', '')
    if activity_filter:
        sessions = sessions.filter(activity_type=activity_filter)

    activity_choices = FitnessSession.ACTIVITY_CHOICES

    context = {
        'sessions': sessions,
        'activity_filter': activity_filter,
        'activity_choices': activity_choices,
    }
    return render(request, 'zenith/fitness_list.html', context)


# ============================================================
#   TOURNAMENT VIEWS
# ============================================================

@login_required
def tournament_list(request):
    """
    Shows all tournaments. Only admins can create tournaments (via Django Admin panel).
    """
    tournaments = Tournament.objects.all()

    context = {
        'tournaments': tournaments,
    }
    return render(request, 'zenith/tournament_list.html', context)

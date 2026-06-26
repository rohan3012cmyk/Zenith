"""
ZENITH - Models
================
Models define the structure of our database tables.
Each class here becomes a table in SQLite.
Each attribute becomes a column in that table.

This is the heart of our data layer - when you run 'python manage.py migrate',
Django reads these models and creates the actual tables in db.sqlite3
"""

from django.db import models
from django.contrib.auth.models import User  # Django's built-in User model


class Game(models.Model):
    """
    Represents a sports game that users can create and join.
    This is the main model of our project.
    
    Example: A cricket game at Gandhi Ground, needs 11 players, on Sunday at 6 AM.
    """

    # Choices for the sport dropdown - makes data consistent
    SPORT_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('volleyball', 'Volleyball'),
        ('badminton', 'Badminton'),
        ('kabaddi', 'Kabaddi'),
        ('kho_kho', 'Kho-Kho'),
        ('marathon', 'Marathon'),
        ('basketball', 'Basketball'),
    ]

    title = models.CharField(max_length=200)         # Short game title, e.g. "Sunday Cricket Match"
    sport = models.CharField(max_length=50, choices=SPORT_CHOICES)  # Restricted to SPORT_CHOICES
    location = models.CharField(max_length=300)       # Where the game will be held
    date = models.DateField()                         # Date of the game
    time = models.TimeField()                         # Start time of the game
    players_needed = models.IntegerField()            # How many players are required
    description = models.TextField(blank=True)        # Optional extra details about the game
    
    # ForeignKey creates a relationship: each game has one host (User)
    # If the user is deleted, their games get deleted too (CASCADE)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_games')
    
    # ManyToMany: a game can have many players, a player can join many games
    players = models.ManyToManyField(User, related_name='joined_games', blank=True)
    
    # auto_now_add=True means this is set automatically when game is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This is what shows up in Django Admin and when you print a Game object
        return f"{self.title} - {self.sport.title()} at {self.location}"

    def players_count(self):
        # Helper method to count how many players have joined
        return self.players.count()

    def is_full(self):
        # Check if game has reached max players
        return self.players.count() >= self.players_needed

    class Meta:
        ordering = ['date', 'time']  # Games sorted by date, then time


class FitnessSession(models.Model):
    """
    Represents a group fitness activity like morning jog or cycling session.
    
    Example: Morning jog at Rajpur Road, every Monday at 6 AM.
    """

    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('jogging', 'Jogging'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
    ]

    title = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    location = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)
    
    # Track when this record was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.activity_type.title()} at {self.location}"

    class Meta:
        ordering = ['date', 'time']  # Sort by date and time


class Tournament(models.Model):
    """
    Represents a local sports tournament.
    Only admin can create/manage tournaments.
    
    Example: Dehradun Inter-Colony Cricket Cup 2024
    """

    SPORT_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('volleyball', 'Volleyball'),
        ('badminton', 'Badminton'),
        ('kabaddi', 'Kabaddi'),
        ('kho_kho', 'Kho-Kho'),
        ('marathon', 'Marathon'),
        ('basketball', 'Basketball'),
    ]

    name = models.CharField(max_length=200)
    sport = models.CharField(max_length=50, choices=SPORT_CHOICES)
    location = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    prize_pool = models.CharField(max_length=100, blank=True)  # e.g. "₹10,000"
    description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.sport.title()}"

    class Meta:
        ordering = ['start_date']  # Show upcoming tournaments first

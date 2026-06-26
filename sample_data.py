"""
ZENITH - Sample Data Script
=============================
Run this script to populate the database with sample data for testing.

Usage: python manage.py shell < sample_data.py
  OR: python manage.py runscript sample_data (if django-extensions installed)
  OR: Just run it manually via Django shell

This creates:
- 2 test users
- 6 sample games
- 4 fitness sessions  
- 3 tournaments
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zenith_project.settings')
django.setup()

from django.contrib.auth.models import User
from zenith.models import Game, FitnessSession, Tournament
from datetime import date, time

print("Creating sample data for ZENITH...")

# ---- Create Users ----
if not User.objects.filter(username='player1').exists():
    user1 = User.objects.create_user(
        username='player1',
        email='player1@zenith.com',
        password='test1234',
        first_name='Rahul'
    )
    print("Created user: player1 (password: test1234)")
else:
    user1 = User.objects.get(username='player1')

if not User.objects.filter(username='player2').exists():
    user2 = User.objects.create_user(
        username='player2',
        email='player2@zenith.com',
        password='test1234',
        first_name='Priya'
    )
    print("Created user: player2 (password: test1234)")
else:
    user2 = User.objects.get(username='player2')

# ---- Create Sample Games ----
games_data = [
    {
        'title': 'Sunday Morning Cricket',
        'sport': 'cricket',
        'location': 'Gandhi Park Ground, Dehradun',
        'date': date(2025, 4, 6),
        'time': time(6, 30),
        'players_needed': 11,
        'description': 'Friendly cricket match. Bring your own bat and pads. All skill levels welcome!',
        'host': user1
    },
    {
        'title': 'Evening Football Match',
        'sport': 'football',
        'location': 'MDDA Sports Ground, Dehradun',
        'date': date(2025, 4, 7),
        'time': time(17, 30),
        'players_needed': 10,
        'description': 'Casual 5-a-side football. Just bring sports shoes!',
        'host': user2
    },
    {
        'title': 'Badminton Doubles Tournament Practice',
        'sport': 'badminton',
        'location': 'Sports Complex, Rajpur Road',
        'date': date(2025, 4, 8),
        'time': time(7, 0),
        'players_needed': 4,
        'description': 'Looking for doubles partners. Rackets available.',
        'host': user1
    },
    {
        'title': 'Kabaddi Practice Session',
        'sport': 'kabaddi',
        'location': 'Local Ground near Prem Nagar',
        'date': date(2025, 4, 10),
        'time': time(5, 30),
        'players_needed': 14,
        'description': 'Traditional Kabaddi game. Come ready to sweat!',
        'host': user2
    },
    {
        'title': 'Basketball 3v3',
        'sport': 'basketball',
        'location': 'Survey of India Court, Dehradun',
        'date': date(2025, 4, 12),
        'time': time(16, 0),
        'players_needed': 6,
        'description': 'Quick 3v3 game. Anyone can join!',
        'host': user1
    },
    {
        'title': 'Volleyball on the Beach',
        'sport': 'volleyball',
        'location': 'Rishikesh Beach, Rishikesh',
        'date': date(2025, 4, 13),
        'time': time(9, 0),
        'players_needed': 12,
        'description': 'Beach volleyball casual game. Come with friends!',
        'host': user2
    },
]

for g in games_data:
    if not Game.objects.filter(title=g['title']).exists():
        Game.objects.create(**g)
        print(f"Created game: {g['title']}")

# ---- Create Fitness Sessions ----
fitness_data = [
    {
        'title': 'Morning Jog Group',
        'activity_type': 'jogging',
        'location': 'Rajpur Road, Dehradun',
        'date': date(2025, 4, 5),
        'time': time(6, 0),
        'description': 'Daily morning jog group. Pace: easy. Distance: 5km approx.'
    },
    {
        'title': 'Cycling to Mussoorie',
        'activity_type': 'cycling',
        'location': 'Starts at Clock Tower, Dehradun',
        'date': date(2025, 4, 6),
        'time': time(5, 30),
        'description': 'Weekend cycling trip to Mussoorie. 35km, medium difficulty. Bring water and snacks.'
    },
    {
        'title': 'Evening Walk - Sahastradhara Road',
        'activity_type': 'walking',
        'location': 'Sahastradhara Road, Dehradun',
        'date': date(2025, 4, 7),
        'time': time(18, 0),
        'description': 'Evening group walk. 3km relaxed pace. Great for stress relief!'
    },
    {
        'title': 'Sprint Training',
        'activity_type': 'running',
        'location': 'Forest Research Institute Track, Dehradun',
        'date': date(2025, 4, 9),
        'time': time(6, 30),
        'description': 'Sprint intervals for intermediate runners. Bring proper running shoes.'
    },
]

for f in fitness_data:
    if not FitnessSession.objects.filter(title=f['title']).exists():
        FitnessSession.objects.create(**f)
        print(f"Created fitness session: {f['title']}")

# ---- Create Tournaments ----
tournaments_data = [
    {
        'name': 'Dehradun Inter-Colony Cricket Cup 2025',
        'sport': 'cricket',
        'location': 'Gandhi Park Ground, Dehradun',
        'start_date': date(2025, 5, 1),
        'end_date': date(2025, 5, 10),
        'prize_pool': '₹15,000',
        'description': 'Annual inter-colony cricket tournament. Teams of 11. Registration open until April 25th.'
    },
    {
        'name': 'Uttarakhand Open Badminton Championship',
        'sport': 'badminton',
        'location': 'Indoor Sports Hall, Parade Ground',
        'start_date': date(2025, 5, 15),
        'end_date': date(2025, 5, 17),
        'prize_pool': '₹8,000',
        'description': 'Open to all age groups. Separate categories for men, women, and mixed doubles.'
    },
    {
        'name': 'City Football League - Summer Edition',
        'sport': 'football',
        'location': 'MDDA Sports Complex, Dehradun',
        'start_date': date(2025, 6, 1),
        'end_date': date(2025, 6, 20),
        'prize_pool': '₹20,000',
        'description': '5-a-side football league. 16 teams. Round robin + knockout format.'
    },
]

for t in tournaments_data:
    if not Tournament.objects.filter(name=t['name']).exists():
        Tournament.objects.create(**t)
        print(f"Created tournament: {t['name']}")

print("\n✅ Sample data created successfully!")
print("\nTest accounts:")
print("  Username: player1  | Password: test1234")
print("  Username: player2  | Password: test1234")
print("\nAdmin: python manage.py createsuperuser")
print("Run server: python manage.py runserver")

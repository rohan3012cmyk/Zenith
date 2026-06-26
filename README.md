# ⚡ ZENITH - Hyperlocal Sports & Fitness Community Platform
### BCA Final Year Project

---

## 📋 Project Overview

ZENITH is a web application that helps local people organize and discover sports games and fitness activities.

**Tech Stack:** Python + Django + SQLite + HTML + CSS

---

## 🚀 Setup Instructions (Step by Step)

### Step 1: Install Python
Download Python 3.10+ from https://python.org
Make sure to check "Add Python to PATH" during installation.

### Step 2: Create a Virtual Environment
Open terminal/command prompt in the project folder:
```
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 3: Install Django
```
pip install -r requirements.txt
```

### Step 4: Set Up the Database
```
python manage.py makemigrations
python manage.py migrate
```
This creates the `db.sqlite3` file with all tables.

### Step 5: Create Admin Account
```
python manage.py createsuperuser
```
Enter your preferred username, email, and password.

### Step 6: Load Sample Data (Optional but Recommended)
```
python sample_data.py
```
This creates test users and sample games/fitness/tournament data.

### Step 7: Start the Server
```
python manage.py runserver
```
Open your browser and go to: **http://127.0.0.1:8000/**

---

## 🔑 Test Accounts (after running sample_data.py)

| Username | Password  |
|----------|-----------|
| player1  | test1234  |
| player2  | test1234  |

**Admin Panel:** http://127.0.0.1:8000/admin/
Use the superuser account you created.

---

## 📁 Project Structure

```
zenith_project/
├── manage.py                   # Django management commands
├── requirements.txt            # Project dependencies  
├── sample_data.py              # Script to add test data
├── db.sqlite3                  # SQLite database (created after migrate)
│
├── zenith_project/             # Main project configuration
│   ├── settings.py             # All project settings
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py                 # Web server gateway
│
└── zenith/                     # Our main app
    ├── models.py               # Database models (Game, FitnessSession, Tournament)
    ├── views.py                # All view functions (business logic)
    ├── urls.py                 # App URL patterns
    ├── forms.py                # Form classes
    ├── admin.py                # Admin panel configuration
    │
    ├── templates/zenith/       # HTML templates
    │   ├── base.html           # Base template (navbar, footer)
    │   ├── home.html           # Landing page
    │   ├── login.html          # Login page
    │   ├── register.html       # Registration page
    │   ├── dashboard.html      # Main dashboard
    │   ├── games_list.html     # Browse all games
    │   ├── game_detail.html    # Single game details
    │   ├── create_game.html    # Create game form
    │   ├── edit_game.html      # Edit game form
    │   ├── delete_game.html    # Delete confirmation
    │   ├── my_games.html       # User's games
    │   ├── fitness_list.html   # Fitness sessions
    │   └── tournament_list.html # Tournaments
    │
    └── static/zenith/css/
        └── style.css           # All styling
```

---

## 🗂️ Module Summary

### 1. Authentication Module
- Register, Login, Logout
- Uses Django's built-in `auth` system
- Session-based authentication

### 2. Dashboard Module
- Shows stats: total games, fitness sessions, tournaments
- Quick navigation cards
- Recent games preview

### 3. Games Module (Main Feature)
- Create, Read, Update, Delete games
- Join/Leave functionality
- Search and filter by sport
- Player management with ManyToMany relationship

### 4. Fitness Module
- Browse fitness sessions
- Filter by activity type

### 5. Tournament Module
- View tournaments
- Admin-managed via Django Admin

---

## 📌 Key Django Concepts Used

| Concept | Where Used |
|---------|-----------|
| Models | zenith/models.py |
| Views (FBV) | zenith/views.py |
| Templates | zenith/templates/ |
| Forms | zenith/forms.py |
| URL Routing | zenith/urls.py |
| ORM Queries | views.py (filter, get, all) |
| Authentication | login_required decorator |
| Admin | zenith/admin.py |
| Messages | Flash notifications |
| CSRF Protection | {% csrf_token %} in forms |

---

*Developed as BCA Final Year Project*

"""
ZENITH - Forms
===============
Forms handle user input - they validate data before saving to database.
Django forms make it easy to create HTML forms and validate them.

Using forms means we don't have to manually check if fields are empty,
if dates are valid, etc. Django handles all of that for us!
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Game


class RegisterForm(UserCreationForm):
    """
    Extends Django's built-in UserCreationForm to add email field.
    UserCreationForm already handles username, password, and password confirmation.
    We just add email on top of that.
    """
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-input'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # These fields will appear in the form in this order

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes and placeholders to each field
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Choose a username',
            'class': 'form-input'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Create a password',
            'class': 'form-input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password',
            'class': 'form-input'
        })

    def save(self, commit=True):
        # Override save to also store the email
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class GameForm(forms.ModelForm):
    """
    Form for creating and editing a Game.
    ModelForm automatically creates form fields from the model fields.
    We just need to specify which fields to include.
    """

    class Meta:
        model = Game
        # Exclude 'host' and 'players' because we set those in the view, not by user input
        fields = ['title', 'sport', 'location', 'date', 'time', 'players_needed', 'description']
        
        # Widgets let us customize how each field looks in HTML
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Sunday Morning Cricket',
                'class': 'form-input'
            }),
            'sport': forms.Select(attrs={
                'class': 'form-input'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g. Gandhi Park Ground, Dehradun',
                'class': 'form-input'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',   # HTML5 date picker
                'class': 'form-input'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',   # HTML5 time picker
                'class': 'form-input'
            }),
            'players_needed': forms.NumberInput(attrs={
                'min': '2',
                'max': '50',
                'placeholder': 'How many players needed?',
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Add any extra details about the game...',
                'class': 'form-input'
            }),
        }

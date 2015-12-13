"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS.
    """
    username = forms.CharField(
            max_length=254,
            label=_("User name"),
            widget=forms.TextInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('User name')
                    }
            )
    )
    password = forms.CharField(
            label=_("Password"),
            widget=forms.PasswordInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('Password')
                    }
            )
    )


class BootstrapRegistrationForm(RegistrationForm):
    """New user registration form.
    """
    first_name = forms.CharField(
            label=_("First name"),
            widget=forms.TextInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('First name')
                    }
            )
    )
    last_name = forms.CharField(
            label=_("Last name"),
            widget=forms.TextInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('Last name')
                    }
            )
    )
    username = forms.CharField(
            label=_("User name"),
            widget=forms.TextInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('User name')
                    }
            )
    )
    email = forms.EmailField(
            label=_("Email"),
            widget=forms.EmailInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('Email')
                    }
            )
    )
    password1 = forms.CharField(
            label=_("Password"),
            widget=forms.PasswordInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('Password')
                    }
            )
    )
    password2 = forms.CharField(
            label=_("Repeat password"),
            widget=forms.PasswordInput(
                    {
                        'class': 'form-control',
                        'placeholder': _('Repeat password')
                    }
            )
    )

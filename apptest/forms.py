from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICE_LIST = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class EngagementsForms(forms.Form):
    current_status = forms.ChoiceField(choices=CHOICE_LIST)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

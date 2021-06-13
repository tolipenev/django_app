from django import forms

CHOICE_LIST = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class EngagementsForms(forms.Form):
    current_status = forms.ChoiceField(choices=CHOICE_LIST)
# Inside forms.py
from django import forms
from .models import BGMI_Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = BGMI_Team
        fields = ['team_name', 'player_1', 'player_2', 'player_3', 'player_4', 'ph_no']

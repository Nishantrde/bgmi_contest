# Inside forms.py
from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'member_1', 'member_2', 'member_3', 'member_4', 'ph_no']

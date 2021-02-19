from django import forms
from .models import Meeting, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

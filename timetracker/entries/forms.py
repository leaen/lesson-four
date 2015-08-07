from django import forms

from .models import Project
from .models import Client

class ClientForm(forms.Form):
    name = forms.CharField()

class ProjectForm(forms.Form):
    name = forms.CharField()
    client = forms.ModelChoiceField(queryset=Client.objects.all())

class EntryForm(forms.Form):
    start = forms.DateTimeField(label="Start Time", help_text="Format: 2006-10-25 14:30")
    end = forms.DateTimeField(label="End Time", help_text="Format: 2006-10-25 14:30")
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField()

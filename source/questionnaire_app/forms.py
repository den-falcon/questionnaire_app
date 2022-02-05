from django import forms
from django.forms import widgets

from questionnaire_app.models import Poll


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={'class': 'form-control'}))


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []

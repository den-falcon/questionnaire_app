from django import forms
from django.forms import widgets, TextInput

from questionnaire_app.models import Poll, Choice


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={'class': 'form-control'}))


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []
        widgets = {
            'question': TextInput(attrs={'class': 'form-control', 'style': 'max-width: 30rem;'})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']
        widgets = {
            'answer': TextInput(attrs={'class': 'form-control', 'style': 'max-width: 30rem;'})
        }
        labels = {
            'answer': 'Добавить вариант ответа:'
        }

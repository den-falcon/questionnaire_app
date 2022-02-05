from django import forms

from questionnaire_app.models import Poll


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []

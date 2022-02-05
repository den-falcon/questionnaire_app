from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from questionnaire_app.forms import AnswerForm
from questionnaire_app.models import Answer, Poll


class AnswerCreate(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answers/answer-create.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(pk=self.kwargs.get('pk'), **self.get_form_kwargs())  # self.request.pk

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll-view', pk=poll.pk)

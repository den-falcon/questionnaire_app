from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from questionnaire_app.forms import ChoiceForm
from questionnaire_app.models import Choice, Poll


class ChoiceCreate(CreateView):
    model = Choice
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll-view', pk=poll.pk)


class ChoiceUpdate(UpdateView):
    model = Choice
    template_name = 'choices/choice-update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse("poll-view", kwargs={"pk": self.object.poll.pk})


class ChoiceDelete(DeleteView):
    model = Choice
    template_name = 'choices/choice-delete.html'

    def get_success_url(self):
        return reverse("poll-view", kwargs={"pk": self.object.poll.pk})

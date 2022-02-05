from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from questionnaire_app.forms import PollForm
from questionnaire_app.models import Poll
from questionnaire_app.views.base import SearchView


class PollsView(SearchView):
    model = Poll
    context_object_name = "polls"
    template_name = "polls/polls-view.html"
    ordering = '-datetime'
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ['question__icontains']


class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "polls/polls-create.html"


class PollUpdate(UpdateView):
    model = Poll
    template_name = 'polls/polls-update.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse("index")  # kwargs={"pk": self.object.pk})


class PollDelete(DeleteView):
    model = Poll
    template_name = 'polls/poll-delete.html'
    success_url = reverse_lazy('index')

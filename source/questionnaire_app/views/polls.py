from django.views.generic import CreateView

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

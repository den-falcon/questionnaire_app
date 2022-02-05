from django.urls import path

from questionnaire_app.views.polls import PollsView, PollCreate

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('poll/create/', PollCreate.as_view(), name='poll-create'),
]

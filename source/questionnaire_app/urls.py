from django.urls import path

from questionnaire_app.views.answers import AnswerCreate
from questionnaire_app.views.choices import ChoiceCreate, ChoiceUpdate, ChoiceDelete
from questionnaire_app.views.polls import PollsView, PollCreate, PollUpdate, PollDelete, PollView

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll-view'),
    path('poll/create/', PollCreate.as_view(), name='poll-create'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='poll-update'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll-delete'),
    path('poll/<int:pk>/choice/create/', ChoiceCreate.as_view(), name='choice-create'),
    path('choice/<int:pk>/update/', ChoiceUpdate.as_view(), name='choice-update'),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='choice-delete'),
    path('poll/<int:pk>/answer/create/', AnswerCreate.as_view(), name='answer-create'),
]

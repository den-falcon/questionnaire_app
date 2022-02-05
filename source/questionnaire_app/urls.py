from django.urls import path

from questionnaire_app.views.polls import PollsView, PollCreate, PollUpdate, PollDelete, PollView

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('poll/<int:pk>', PollView.as_view(), name='poll-view'),
    path('poll/create/', PollCreate.as_view(), name='poll-create'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='poll-update'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll-delete'),
]

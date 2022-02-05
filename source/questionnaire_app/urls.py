from django.urls import path

from questionnaire_app.views.polls import PollsView

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
]

from django.contrib import admin
from questionnaire_app.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'datetime']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'datetime']
    readonly_fields = ['datetime']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)

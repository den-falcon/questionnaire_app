from django.contrib import admin
from questionnaire_app.models import Pool, Choice


class PoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'datetime']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'datetime']
    readonly_fields = ['datetime']


admin.site.register(Pool, PoolAdmin)
admin.site.register(Choice)

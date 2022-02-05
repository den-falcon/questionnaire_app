from django.db import models
from django.urls import reverse


class Poll(models.Model):
    question = models.CharField(max_length=200, verbose_name="Вопрос")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @staticmethod
    def get_absolute_url():
        return reverse('index')

    def __str__(self):
        return f'{self.question} | {self.datetime}'

    class Meta:
        db_table = 'poll'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    answer = models.CharField(max_length=200, verbose_name="Вариант ответа")
    poll = models.ForeignKey('questionnaire_app.Poll', related_name='choices', on_delete=models.CASCADE,
                             verbose_name='Вопрос')

    def __str__(self):
        return f'{self.answer} | {self.poll}'

    class Meta:
        db_table = 'choice'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answer(models.Model):
    poll = models.ForeignKey('questionnaire_app.Poll', related_name='answers', on_delete=models.CASCADE,
                             verbose_name='Опрос')
    choice = models.ForeignKey('questionnaire_app.Choice', related_name='answers', on_delete=models.CASCADE,
                               verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.poll} | {self.choice}'

    class Meta:
        db_table = 'answers'
        verbose_name = 'Ответ на опрос'
        verbose_name_plural = 'Ответы на опрос'

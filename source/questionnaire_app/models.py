from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200, verbose_name="Вопрос")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.question} | {self.datetime}'

    class Meta:
        db_table = 'poll'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    poll = models.ForeignKey('questionnaire_app.Poll', related_name='choices', on_delete=models.CASCADE,
                             verbose_name='Вопрос')

    def __str__(self):
        return f'{self.answer} | {self.poll}'

    class Meta:
        db_table = 'choice'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

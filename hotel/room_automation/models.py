from django.db import models


class RoomAutomation(models.Model):
    number = models.CharField(verbose_name='Номер', null=False, max_length=5)
    light = models.JSONField(verbose_name='Свет')
    climate = models.JSONField(verbose_name='Климат')

    class Meta:
        verbose_name = 'Автоматизация номера'
        verbose_name_plural = 'Автоматизация номеров'
        ordering = ['number']

    def __str__(self):
        return f'Номер {self.number}'

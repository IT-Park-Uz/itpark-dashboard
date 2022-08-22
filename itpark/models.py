from django.db import models

class ItPark(models.Model):
    admins = models.CharField(max_length=100, verbose_name='Значения')
    filials = models.CharField(max_length=100, verbose_name='Количество филиалов')
    startapps = models.CharField(max_length=100, verbose_name='Стартап-Проектов')
    volume = models.CharField(max_length=100, verbose_name='Объем финансирования')
    incubation = models.CharField(max_length=100, verbose_name='Инкубацинные центры')
    trained = models.CharField(max_length=100, verbose_name='Обучено госслужащих')
    events = models.CharField(max_length=100, verbose_name='Количество мероприятий')
    partners = models.CharField(max_length=100, verbose_name='Количество партнеров')
    participants = models.CharField(max_length=100, verbose_name='Количество участников конкурсов')
    staff = models.CharField(max_length=100, verbose_name='Сотрудников IT Park')

    class Meta:
        verbose_name = 'Значение Dashboard'
        verbose_name_plural = 'Значения Dashboard'

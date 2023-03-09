from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Human(models.Model):
    class Meta:
        verbose_name = 'Люди'
        verbose_name_plural = 'Люди'
        ordering = ['age']

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateTimeField()
    is_live = models.BooleanField()
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессии')


class Profession(models.Model):
    title = models.CharField(max_length=50, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('view_human', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Профессии'
        verbose_name_plural = 'Профессия'
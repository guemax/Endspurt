from django.db import models


class Class(models.Model):
    class_level = models.IntegerField(verbose_name='Klassenstufe')
    parallel_class = models.CharField(max_length=1, verbose_name='Parallelklasse')

    class Meta:
        verbose_name = 'Klasse'
        verbose_name_plural = 'Klassen'

    def __str__(self) -> str:
        return str(self.class_level) + self.parallel_class

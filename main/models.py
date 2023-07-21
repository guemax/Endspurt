from django.db import models


class Class(models.Model):
    class_level = models.IntegerField(verbose_name='Klassenstufe')
    parallel_class = models.CharField(max_length=1, verbose_name='Parallelklasse')

    class Meta:
        verbose_name = 'Klasse'
        verbose_name_plural = 'Klassen'

    def __str__(self) -> str:
        return str(self.class_level) + self.parallel_class

    def save(self, *args, **kwargs):
        self.parallel_class = self.parallel_class.lower()
        super().save(*args, **kwargs)


class Station(models.Model):
    sport = models.CharField(max_length=50, verbose_name='Sportart')

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stationen'

    def __str__(self) -> str:
        return self.sport

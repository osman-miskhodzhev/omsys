from django.db import models


class Food(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=120,
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=100_000,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

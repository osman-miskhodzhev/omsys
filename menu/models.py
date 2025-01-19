from django.db import models


class Food(models.Model):
    name = models.CharField(
        max_length=120
    )
    price = models.DecimalField(
        max_digits=100_000,
        decimal_places=2,
    )

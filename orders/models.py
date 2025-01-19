from django.db import models

from menu.models import Food


class Order(models.Model):
    PENDING = 'в ожидании'
    READY = 'готово'
    PAID_FOR = 'оплачено'

    table_number = models.DecimalField(
        verbose_name='Номер стола',
        max_digits=100,
        decimal_places=0,
    )
    total_price = models.DecimalField(
        verbose_name='общая стоимость заказа',
        max_digits=100_000,
        decimal_places=2,
        default=0,
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        max_length=3,
        default=PENDING,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ № {self.id} ({self.created_at})"

    def search_orders(search_query):
        if not search_query:
            return Order.objects.all()
        return Order.objects.filter(
            models.Q(table_number__icontains=search_query) |
            models.Q(status__icontains=search_query)
        )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='food_items'
    )
    quantity = models.PositiveIntegerField(default=1)

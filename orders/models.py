import datetime

from django.db import models

from menu.models import Food

class Order(models.Model):
    PENDING = 'в ожидании'
    READY = 'готово'
    PAID_FOR = 'оплачено'

    table_number = models.DecimalField(
        max_digits=100,
        decimal_places=0,
    )
    total_price = models.DecimalField(
        max_digits=100_000,
        decimal_places=2,
        default=0,
    )
    status = models.CharField(
        max_length=3,
        default=PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def search_orders(search_query):
        result = Order.objects.filter(
            models.Q(table_number__icontains=search_query) |
            models.Q(status__icontains=search_query)
        )
        if not search_query:
            return Order.objects.all()
        return Order.objects.filter(
            models.Q(table_number__icontains=search_query) |
            models.Q(status__icontains=search_query)
        )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_items')
    quantity = models.PositiveIntegerField(default=1)

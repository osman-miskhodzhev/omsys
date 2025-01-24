from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from menu.models import Food


class Order(models.Model):
    PENDING = 'pending'
    READY = 'approved'
    PAID_FOR = 'cancelled'

    table_number = models.PositiveIntegerField(
        verbose_name='Номер стола',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    total_price = models.DecimalField(
        verbose_name='общая стоимость заказа',
        max_digits=100_000,
        decimal_places=2,
        default=0,
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        max_length=9,
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

    def items(self):
        return OrderItem.objects.filter(order_id=self.pk)

    def get_revenue(start_time, end_time):
        if start_time and end_time:
            orders = Order.objects.filter(
                status='оплачено',
                created_at__range=[start_time, end_time]
            )

            total_revenue = sum([order.total_price for order in orders])
            total_orders = len(orders)
            return (total_orders, total_revenue)

    def update_total_price(self):
        order_items = self.items()
        if not order_items.exists():
            raise Http404("Нет связанных пунктов заказа.")

        total_price = sum(
            item.food.price * item.quantity for item in order_items
        )
        self.total_price = total_price
        self.save()


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

    class Meta:
        verbose_name = 'Пункт заказа'
        verbose_name_plural = 'Пункты заказов'

    def __str__(self):
        return f"заказ {self.order.id} | {self.food.name} {self.quantity} шт."
    
    def add_item(order, food, quantity):
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            food=food,
            defaults={'quantity': quantity}
        )

        if not created:
            order_item.quantity += quantity
            order_item.save()

        return order_item, created

from django.urls import path
from .views import (
    OrdersView,
    OrderCreate,
    OrderDelete,
    OrderStatusUpdate,
    OrderItemsAdd,
    OrderTotalPriceUpdate,
    RevenueView,
)

app_name = 'orders'

urlpatterns = [
    path('', OrdersView.as_view(), name='orders-list'),
    path('order_create/', OrderCreate.as_view(), name='order-create'),
    path('order_delete/<int:pk>/', OrderDelete.as_view(), name='order-delete'),
    path(
        'order_status_update/<int:pk>/<str:status>/',
        OrderStatusUpdate.as_view(),
        name='order-update-status'
    ),

    path(
        'order_items_add/<int:pk>/',
        OrderItemsAdd.as_view(),
        name='order-items-add'
    ),
    path(
        'order_update_total/<int:pk>/',
        OrderTotalPriceUpdate.as_view(),
        name='order-update-total'
    ),
    path('revenue/', RevenueView.as_view(), name='revenue_report'),
]

from django.urls import path, include

from rest_framework import routers

from .views import (
    FoodListAPIView,
    OrderModelViewSet,
    OrderItemModelViewSet,
    OrderSearchView,
    CalculateRevenueView,
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'orders', OrderModelViewSet)
router.register(r'orders-itmes', OrderItemModelViewSet)

urlpatterns = [
    path('menu/', FoodListAPIView.as_view(), name='menu-api'),
    path('orders/search/', OrderSearchView.as_view(), name='order-search'),
    path(
        'calculate-revenue/',
        CalculateRevenueView.as_view(),
        name='calculate-revenue'
    ),
    path('', include(router.urls)),
]

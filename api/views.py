from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from menu.models import Food
from menu.serializers import FoodSerializer

from orders.models import Order, OrderItem
from orders.serializers import (
    OrderSerializer,
    OrderItemSerializer,
    RevenueRequestSerializer
)


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderSearchView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)
        if search_query:
            return Order.search_orders(search_query)
        return Order.objects.none()


class CalculateRevenueView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RevenueRequestSerializer(data=request.data)

        if serializer.is_valid():
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']

            data = Order.get_revenue(start_time, end_time)

            if data:
                total_orders, total_revenue = data
            return Response(
                {
                    'total_revenue': total_revenue,
                    'total_orders': total_orders
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

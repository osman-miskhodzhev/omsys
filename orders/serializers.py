from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'order_id',
            'food_id',
            'quantity'
        ]
    def create(self, validated_data):
        print(validated_data)  # Для отладки: убедитесь, что food передается
        return super().create(validated_data)



class OrderSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'table_number',
            'total_price',
            'items',
            'status',
            'created_at',
        ]

    def get_items(self, obj):
        """Вызываем метод items() из модели"""
        items = obj.items()
        return OrderItemSerializer(items, many=True).data


class RevenueRequestSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

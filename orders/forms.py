from django import forms

from .models import Order, OrderItem


class SearchOrder(forms.Form):
    request_text = forms.CharField(label="Поиск заказа", max_length=100)


class AddItems(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'food',
            'quantity'
        ]
        error_messages = {
            'quantity': {
                'required': 'Укажите количество.',
                'invalid': 'Количество должно быть числом.',
                'min_value': 'Количество должно быть больше 0.',
            },
            'food': {
                'required': 'Выберите блюдо',
                'invalid_choice': 'Ошибка при выборе еды.',
            }
        }


class AddOrders(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'table_number',
        ]
        error_messages = {
            'table_number': {
                'required': 'Укажите номер стола.',
                'invalid': 'Неверный тип данных. Введите число',
                'min_value': 'Номер стола должен быть больше 0.',
            },
        }

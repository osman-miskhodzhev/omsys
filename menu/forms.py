from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'name',
            'price',
        ]
        error_messages = {
            'name': {
                'required': 'Введите название блюда',
            },
            'price': {
                'required': 'Выберите блюдо',
                'min_value': 'Количество должно быть больше 0.',
                'invalid': 'Цену нужно указать числом',
            }
        }

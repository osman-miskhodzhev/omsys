from django import forms

from .models import OrderItem

class SearchOrder(forms.Form):
    request_text = forms.CharField(label="Поиск заказа", max_length=100)


class AddItems(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'food',
            'quantity'
        ]

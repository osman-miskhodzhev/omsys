from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Food

class MenuView(TemplateView):
    template_name = 'menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = Food.objects.all()
        return context


class FoodAdd(CreateView):
    template_name = 'food_add.html'
    model = Food
    fields = [
        'name',
        'price',
    ]
    success_url = reverse_lazy('menu:menu-list')

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.contrib import messages


from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    DeleteView,
    FormView,
)

from .models import Order, OrderItem
from .forms import SearchOrder, AddItems, AddOrders, RevenueForm


def custom_404(request, exception):
    return render(request, '404.html', status=404)


class OrdersView(TemplateView):
    template_name = 'orders/orders.html'

    def get_context_data(self, **kwargs):
        search_query = self.request.GET.get('request_text', '')
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.search_orders(search_query)
        context["search_form"] = SearchOrder()
        context["orders_items"] = OrderItem()
        print(self.request)
        return context


class OrderCreate(FormView):
    template_name = 'orders/order_add.html'
    form_class = AddOrders

    def get_success_url(self):
        return reverse_lazy(
            'orders:order-items-add',
            kwargs={'pk': self.order.pk}
        )

    def form_valid(self, form):
        self.order = form.save()
        return super().form_valid(form)


class OrderItemsAdd(FormView):
    template_name = 'orders/add_items.html'
    form_class = AddItems

    def form_valid(self, form):
        try:
            order = Order.objects.get(pk=self.kwargs['pk'])
            food = form.cleaned_data['food']
            quantity = form.cleaned_data['quantity']

            OrderItem.add_item(order=order, food=food, quantity=quantity)

            messages.success(self.request, "Пункт заказа успешно добавлен.")
            return super().form_valid(form)
        except Order.DoesNotExist:
            messages.error(self.request, "Такого заказа не существует.")
            return redirect('orders:orders-list')
        

    def get_success_url(self):
        return reverse(
            'orders:order-items-add',
            kwargs={'pk': self.kwargs['pk']}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs['pk'])
        context['items'] = OrderItem.objects.filter(order=self.kwargs['pk'])
        return context


class OrderDelete(DeleteView):
    template_name = 'orders/delete_confirm.html'
    model = Order
    success_url = reverse_lazy('orders:orders-list')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            messages.error(
                self.request,
                "Нет такого заказа"
            )
            return redirect('orders:orders-list')


class OrderStatusUpdate(View):
    def post(self, request, pk, status, *args, **kwargs):
        try:
            order = get_object_or_404(Order, pk=pk)

            if status not in ['pending', 'approved', 'cancelled']:
                messages.error(request, f"Некорректный статус: {status}")
                return redirect('orders:orders-list')
            order.status = status
            order.save()
            messages.success(request, f"Обнавлен статус заказа {pk}")
            return redirect('orders:orders-list')

        except Http404:
            messages.error(
                request,
                "Нет такого объекта"
            )
            return redirect('orders:orders-list')


class OrderTotalPriceUpdate(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            order = get_object_or_404(Order, pk=pk)
            order.update_total_price()
        except Http404:
            messages.error(
                request,
                "Такого заказа не существует или отсутствуют пункты заказа."
            )
            return redirect('orders:orders-list')

        except Exception as e:
            messages.error(request, f"Ошибка: {e}")
            return redirect('orders:orders-list')
        
        messages.success(request, "Общая стоимость заказа успешно обновлена.")
        return redirect('orders:orders-list')


class RevenueView(View):
    template_name = 'orders/revenue.html'
    def get(self, request):
        form = RevenueForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            total_revenue = 0
            total_orders = 0
            start_time = self.request.GET.get('start_time')
            end_time = self.request.GET.get('end_time')
            data = Order.get_revenue(Order.PAID_FOR, start_time, end_time)
            total_orders, total_revenue = data

            context['total_revenue'] = total_revenue
            context['total_orders'] = total_orders
            context['start_time'] = start_time
            context['end_time'] = end_time

        return render(request, self.template_name, context)

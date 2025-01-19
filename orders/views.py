from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import Http404

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView

from .models import Order, OrderItem
from .forms import SearchOrder, AddItems


def custom_404(request, exception):
    return render(request, '404.html', status=404)


class OrdersView(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        search_query = self.request.GET.get('request_text', '')
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.search_orders(search_query)
        context["search_form"] = SearchOrder()
        context["orders_items"] = OrderItem()
        return context


class OrderCreate(CreateView):
    template_name = 'order_add.html'
    model = Order
    fields = [
        'table_number',
    ]

    def get_success_url(self):
        return reverse_lazy(
            'orders:order-items-add',
            kwargs={'pk': self.object.pk}
        )


class OrderItemsAdd(FormView):
    template_name = 'add_items.html'
    form_class = AddItems

    def get_order(self):
        return Order.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        order = self.get_order()
        food = form.cleaned_data['food']
        quantity = form.cleaned_data['quantity']

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            food=food,
            defaults={'quantity': quantity}
        )

        if not created:
            order_item.quantity += quantity
            order_item.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'orders:order-items-add',
            kwargs={'pk': self.kwargs['pk']}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.get_order()
        context['items'] = OrderItem.objects.filter(order=self.kwargs['pk'])
        return context


class OrderDelete(DeleteView):
    template_name = 'delete_confirm.html'
    model = Order
    success_url = reverse_lazy('orders:orders-list')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            raise Http404("Объект не найден, удаление невозможно.")


class OrderStatusUpdate(View):
    def post(self, request, pk, status, *args, **kwargs):
        order = get_object_or_404(Order, pk=pk)
        order.status = status
        order.save()
        return redirect('orders:orders-list')


class OrderTotalPriceUpdate(View):
    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, pk=pk)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(
            item.food.price * item.quantity for item in order_items
        )
        order.total_price = total_price
        order.save()

        return redirect('orders:orders-list')


class RevenueReportView(TemplateView):
    template_name = 'revenue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_revenue = 0
        total_orders = 0
        orders = None

        start_time = self.request.GET.get('start_time')
        end_time = self.request.GET.get('end_time')

        if start_time and end_time:
            orders = Order.objects.filter(
                status='оплачено',
                created_at__range=[start_time, end_time]
            )

            total_revenue = sum([order.total_price for order in orders])
            total_orders = len(orders)

        context['total_revenue'] = total_revenue
        context['total_orders'] = total_orders
        context['orders'] = orders
        context['start_time'] = start_time
        context['end_time'] = end_time

        return context

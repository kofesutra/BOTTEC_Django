from django.shortcuts import render
from django.views.generic import ListView

from user.models import CompletedOrder


def index_page(request):

    get_orders = CompletedOrder.objects.all()
    data = {'data': get_orders, 'title': 'Статистика заказов', 'h1': 'Оплаченные заказы'}

    return render(request, 'index.html', data)

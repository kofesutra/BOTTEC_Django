from asgiref.sync import sync_to_async
from django.db import models


class CompletedOrder(models.Model):
    using = 'orders_psql'

    class Meta:
        db_table = 'orders'

    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=20, blank=False, default='none')
    goods = models.CharField(max_length=50, blank=False, default='none')
    size = models.CharField(max_length=50, blank=False, default='none')
    quantity = models.IntegerField(default=0)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fullname = models.CharField(max_length=50, blank=False, default='none')
    phone = models.CharField(max_length=14, blank=False, default='none')
    address = models.CharField(max_length=100, blank=False, default='none')

    objects = models.Manager()


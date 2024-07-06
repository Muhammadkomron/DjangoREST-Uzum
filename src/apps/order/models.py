from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.order.choices import OrderStatusChoices
from apps.order.managers import OrderManager
from apps.shared.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')
    status = models.PositiveSmallIntegerField(choices=OrderStatusChoices.choices)

    objects = OrderManager()

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.id}'

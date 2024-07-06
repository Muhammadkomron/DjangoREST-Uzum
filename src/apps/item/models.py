from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.item.managers import ItemManager
from apps.shared.models import BaseModel


class Item(BaseModel):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='items')
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='items')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='items')

    objects = ItemManager()

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    def __str__(self):
        return f'{self.id}'

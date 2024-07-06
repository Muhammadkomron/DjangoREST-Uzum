from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.product.managers import ProductManager
from apps.shared.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.id}'

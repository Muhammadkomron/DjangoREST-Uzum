from django.db import models


class OrderStatusChoices(models.IntegerChoices):
    created = 1, 'Created'
    finished = 2, 'Finished'
    cancelled = 3, 'Cancelled'
    refunded = 4, 'Refunded'

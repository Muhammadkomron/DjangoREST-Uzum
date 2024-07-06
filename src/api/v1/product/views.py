from rest_framework import mixins, viewsets

from api.v1.product.serializers import ProductModelSerializer
from apps.product.models import Product


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    http_method_names = ('get', 'post', 'put', 'delete', 'options')

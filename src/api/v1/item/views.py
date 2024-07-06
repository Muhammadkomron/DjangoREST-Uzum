from rest_framework import mixins, viewsets

from api.v1.item.serializers import ItemModelSerializer
from apps.item.models import Item


class ItemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ItemModelSerializer
    queryset = Item.objects.all()
    http_method_names = ('get', 'post', 'put', 'delete', 'options')

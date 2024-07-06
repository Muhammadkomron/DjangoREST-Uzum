from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.order.serializers import OrderModelSerializer, OrderPayModelSerializer
from apps.order.models import Order
from uzum.client import ApiClient


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()
    http_method_names = ('get', 'post', 'put', 'patch', 'options')
    permission_classes = (IsAuthenticated,)

    @action(methods=['patch'], detail=True, serializer_class=OrderPayModelSerializer)
    def pay(self, request, *args, **kwargs):
        instance = self.get_object()
        client = ApiClient()
        amount = sum([float(item.product.price) for item in instance.items.all()])
        client.register(
            amount=amount, client_id=instance.user.id, currency=860, order_number=instance.id,
            success_url='https://example.com', failure_url='https://example.com',
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

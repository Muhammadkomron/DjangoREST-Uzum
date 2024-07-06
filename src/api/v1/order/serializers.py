from rest_framework import serializers

from api.v1.item.serializers import ItemModelSerializer
from apps.item.models import Item
from apps.order.choices import OrderStatusChoices
from apps.order.models import Order
from apps.product.models import Product


class OrderModelSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True)
    status = serializers.ChoiceField(choices=OrderStatusChoices.choices, read_only=True)
    items = ItemModelSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'products',
            'status',
            'items',
        )

    def create(self, validated_data):
        user = self.context.get('request').user
        products = validated_data.pop('products')
        validated_data.update(user=user, status=OrderStatusChoices.created)
        order = super().create(validated_data)
        Item.objects.bulk_create((Item(product=product, order=order, user=user) for product in products))
        return order


class OrderPayModelSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=OrderStatusChoices.choices, read_only=True)
    items = ItemModelSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'items',
        )

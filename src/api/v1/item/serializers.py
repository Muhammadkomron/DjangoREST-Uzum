from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.v1.product.serializers import ProductModelSerializer
from apps.item.models import Item


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )


class ItemModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    user = UserModelSerializer()

    class Meta:
        model = Item
        fields = (
            'id',
            'product',
            'order',
            'user',
        )

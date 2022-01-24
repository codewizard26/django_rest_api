from . models import Order
from api.user.models import CustomUser
from api.product.models import Product
from rest_framework import serializers

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (['user'])
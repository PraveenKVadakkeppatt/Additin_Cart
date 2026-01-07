
from rest_framework import serializers

from orders.models import Orders


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
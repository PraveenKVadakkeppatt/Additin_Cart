

from rest_framework import serializers

from cart.models import Cart, CartItem



class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name',read_only=True)
    price = serializers.CharField(source='product.price',read_only=True)
    tax_percent = serializers.DecimalField(source='product.tax_percent',read_only = True,max_digits=10,decimal_places=2)
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many = True)
    subtotal = serializers.DecimalField(max_digits=10,decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        model = Cart
        fields = '__all__'

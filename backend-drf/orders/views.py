from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import Cart
from orders.models import OrderItem, Orders
from orders.serializers import OrderSerializers
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView
from orders.utilis import send_order_notification
# Create your views here.


class PlaceOrderViews(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        cart = Cart.objects.get(user=request.user)
        # Read shipping address from frontend
        shipping_address = request.data.get("shippingAddress")
        if not cart or cart.items.count() == 0:
            return Response({'error':'Cart is empty'})
        
        # print('grand_total==>',cart.grand_total)
        order = Orders.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total,
            address = shipping_address.get("address"),
            phone = shipping_address.get('phone'),
            city = shipping_address.get('city'),
            state = shipping_address.get('state'),
            zip_code = shipping_address.get('zipcode')
        )

        for item in cart.items.all():
            product = item.product

            if product.stock < item.quantity:
                return Response({'details':f'Only {product.stock} is left for {product.name}'},status=status.HTTP_400_BAD_REQUEST)

            product.stock -= item.quantity
            product.save()

        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price,
                total_price = item.total_price,
            )

        
        cart.items.all().delete()
        cart.save()

        send_order_notification(order)

        serializer = OrderSerializers(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class MyOrderView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializers

    def get_queryset(self):
        return Orders.objects.filter(user = self.request.user)


class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializers

    def get_object(self):
        pk = self.kwargs.get('pk')
        order = get_object_or_404(Orders, pk=pk, user=self.request.user)
        return order
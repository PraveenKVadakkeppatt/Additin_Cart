from django.contrib import admin

from cart import models
from orders.models import OrderItem, Orders

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class Orderadmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Orders,Orderadmin)
# admin.site.register(OrderItem)
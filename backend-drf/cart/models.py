from django.db import models

from product.models import Product
from users.models import User

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user})"
    
    @property
    def subtotal(self):
        subtotal = 0
        for item in self.items.all():
            subtotal += item.product.price * item.quantity
        return subtotal
    
    @property
    def tax_amount(self):
        tax_amount=0
        for item in self.items.all():
            tax_amount += item.product.price*item.quantity * item.product.tax_percent/100
        return tax_amount
    
    @property
    def grand_total(self):
        grand_total = self.subtotal + self.tax_amount
        return grand_total
        
        
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} X {self.quantity} "
    
    @property
    def total_price(self):
        total_price = self.product.price * self.quantity
        return total_price
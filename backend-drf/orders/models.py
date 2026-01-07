from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()

class Orders(models.Model):
    STATUS_CHOICES = [
        ('PENDING','pending'),
        ('CONFIRMED','confirmed'),
        ('DELIVERED','delivered'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10,decimal_places=2)
    grand_total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=25,choices=STATUS_CHOICES,default='PENDING')
    address = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}-{self.user.email}"
     

class OrderItem(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    


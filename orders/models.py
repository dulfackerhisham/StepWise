from django.db import models
from accounts.models import Account
from products.models import ProductItem
from accounts.models import Profile


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Profile, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatus = {
        ('pending', 'pending'),
        ('out for shipping', 'out for shipping'),
        ('completed', 'completed'),
    }
    status = models.CharField(max_length=150, choices=orderstatus, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=250, null=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.id} {self.tracking_no}"
    
    def save(self, *args, **kwargs):
        """
        calculating the total_price of all product with the quantity respectively from cart model
        """
        total_price = 0
        for cart_item in self.user.cart_set.all():
            total_price += cart_item.product.price * cart_item.qty

        self.total_price = total_price
        super(Order, self).save(*args, **kwargs)
    
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f" {self.product} {self.order.tracking_no}"
    


from django.db import models
from accounts.models import Account
from products.models import ProductItem

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductItem, on_delete=models.SET_NULL, null=True)
    qty  = models.PositiveIntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

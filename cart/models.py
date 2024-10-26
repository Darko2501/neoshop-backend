from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    @property
    def total_amount(self):
      total=sum(item.products.price for item in self.cartitems.all())
      return total
    def __str__(self):
        return f"Cart {self.user.username} - {self.total_amount}"
class CartItems(models.Model):
    cart=models.ForeignKey(Cart,related_name='cartitems',on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cart.user}-{self.products}"



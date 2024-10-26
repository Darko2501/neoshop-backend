from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('COMPLETED', 'Completed'),
            ('CANCELLED', 'Cancelled')
        ],
        default='PENDING'
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('UNPAID', 'Unpaid'),
            ('PAID', 'Paid')
        ],
        default='UNPAID'
    )

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



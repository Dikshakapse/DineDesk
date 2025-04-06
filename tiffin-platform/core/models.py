from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Tiffin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tiffin = models.ForeignKey(Tiffin, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.tiffin.name} ({self.quantity})"

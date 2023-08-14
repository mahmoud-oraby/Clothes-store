from django.db import models
from product.models import Product
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        Return a string representation of the user associated with the cart.
        """
        return str(self.user)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        Override the save method to update the product's stock number and save the cart item.
        """
        self.product.stock_number -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation of the cart item, including the associated product title and user.
        """
        return f'{str(self.product.title)} - {str(self.cart.user)}'


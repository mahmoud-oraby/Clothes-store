from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart

@receiver(post_save, sender=get_user_model())
def create_cart_for_new_user(sender, instance, created, **kwargs):
    """
    Signal receiver to create a cart for a newly created user.
    """
    if created:
        Cart.objects.create(user=instance)
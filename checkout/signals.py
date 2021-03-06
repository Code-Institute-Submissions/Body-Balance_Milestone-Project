from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductLineOrder


@receiver(post_save, sender=ProductLineOrder)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineorders update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=ProductLineOrder)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineorders delete
    """
    instance.order.update_total()

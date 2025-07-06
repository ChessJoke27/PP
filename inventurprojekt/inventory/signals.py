from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item, Order

@receiver(post_save, sender=Item)
def create_warranty_order(sender, instance, created, **kwargs):
    if not created:
        return
    warranty_years = 1 if instance.brand.lower() == 'apple' else 2
    due_date = instance.purchase_date + timedelta(days=365 * warranty_years)
    Order.objects.create(
        name=f"Garantieablauf: {instance.name}",
        product=instance,
        due_date=due_date,
    )

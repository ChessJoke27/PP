from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return self.name

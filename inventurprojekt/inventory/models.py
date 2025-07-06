from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    purchase_link = models.URLField(blank=True)
    is_apple = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

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
    # Link orders to products instead of inventory items
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return self.name

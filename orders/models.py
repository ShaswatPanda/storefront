from django.db import models

# Create your models here.
class Order(models.Model):
    time_placed = models.TextField()
    billing_address = models.TextField()
    shipping_address = models.TextField()
    mode_of_payment_used = models.TextField()
    grand_total = models.TextField()
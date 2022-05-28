from django.db import models

# Create your models here.
class Cart(models.Model):
    items = models.TextField()
    item_quantities = models.TextField()
    coupons = models.TextField()
    grand_total = models.TextField()
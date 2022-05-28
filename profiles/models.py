from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    address = models.TextField()
    email = models.TextField()
    phone_number = models.TextField()
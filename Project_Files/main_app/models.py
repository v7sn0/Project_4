from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inquiry(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    custom_request = models.CharField(255)
    date_of_inquiry = models.DateField((""), auto_now=False, auto_now_add=False)


class Product(models.Model):
    supplier_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.CharField(100)
    description = models.CharField(255)
    availability = models.BooleanField(default=False)

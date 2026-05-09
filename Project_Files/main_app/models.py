from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inquiry(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    qty = models.IntegerField()
    custom_request = models.CharField(max_length=255)
    date_of_inquiry = models.DateField((""), auto_now=True)

    def __str__(self):
        return self.customer_id


class Product(models.Model):
    supplier_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.supplier_id

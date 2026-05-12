from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models hereok.


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        CUSTOMER = "Customer", "Customer"
        SUPPLIER = "Supplier", "Supplier"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.CUSTOMER
    )
    email = models.EmailField(unique=True, blank=False)


class Product(models.Model):
    supplier_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.supplier_id


class Inquiry(models.Model):
    customer_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, related_name="inquiries"
    )
    item_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    qty = models.IntegerField()
    custom_request = models.TextField(max_length=500)
    date_of_inquiry = models.DateField((""), auto_now=True)
    accept = models.BooleanField(default=False)
    acknowledgment = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.customer_id


class InquiryStatus(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, null=False)
    # status = models.Choices()
    accept = models.BooleanField(default=False)
    acknowledgment = models.TextField(max_length=500)

    def __str__(self):
        return self.acknowledgment

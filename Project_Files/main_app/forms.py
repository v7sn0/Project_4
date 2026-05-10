from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Inquiry, Product, CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["qty", "custom_request"]  # missing timestamp field + customer id


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["item", "description", "availability"]  # missing supplier id

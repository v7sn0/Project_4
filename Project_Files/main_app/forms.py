from django import forms
from .models import Inquiry, Product


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["qty", "custom_request"]  # missing timestamp field + customer id


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["item", "description", "availability"]  # missing supplier id

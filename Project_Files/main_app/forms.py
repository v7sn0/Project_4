from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Inquiry, Product, InquiryStatus, CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "title",
            "qty",
            "custom_request",
        ]  # missing timestamp field + customer id


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["item", "description", "availability"]  # missing supplier id


class InquiryStatusForm(forms.ModelForm):
    class Meta:
        model = InquiryStatus
        fields = ["inquiry", "accept", "acknowledgment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(self.instance, "accept", False):
            for field in self.fields.values():
                field.widget.attrs["disabled"] = "disabled"


class InquiryUpdate(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["accept", "acknowledgment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(self.instance, "accept", False):
            for field in self.fields.values():
                field.widget.attrs["disabled"] = "disabled"

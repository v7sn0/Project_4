from django import forms
from .models import Inquiry



class InquiryForm(forms.ModelForm):
    class Meta :
        model= Inquiry
        fields = ["qty","custom_request","date_of_inquiry"]

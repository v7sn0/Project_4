from django.shortcuts import render


from .models import Inquiry, Product
from .forms import InquiryForm, ProductForm
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = "/auth/login"


class CreateInquiryView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = "customers/inquiry-form.html"
    success_url = "/"


class UploadProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "suppliers/product-form.html"
    success_url = "/"


class ListProductsView(ListView):
    model = Product
    template_name = "home-customer.html"
    context_object_name = "products"

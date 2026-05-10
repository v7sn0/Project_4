from django.shortcuts import render


from .models import Inquiry, Product, CustomUser
from .forms import InquiryForm, ProductForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    form_class = CustomUserCreationForm
    success_url = "/auth/login"
    model = CustomUser


class CreateInquiryView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.role == "Customer" or self.request.user.is_superuser

    model = Inquiry
    form_class = InquiryForm
    template_name = "customers/inquiry-form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.customer_id = self.request.user
        return super().form_valid(form)


class UploadProductView(UserPassesTestMixin, CreateView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    form_class = ProductForm
    template_name = "suppliers/product-form.html"
    success_url = "/"  # Will be changed

    def form_valid(self, form):
        form.instance.supplier_id = self.request.user
        return super().form_valid(form)


class UpdateProductView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    form_class = ProductForm
    template_name = "suppliers/product-form.html"
    success_url = "/listed-products"  # Will be changed


class ListProductsView(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.role == "Customer" or self.request.user.is_superuser

    model = Product
    template_name = "home-customer.html"
    context_object_name = "products"


class UploadedProductsList(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    template_name = "home-supplier.html"
    context_object_name = "products"


class DeleteProduct(UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    success_url = "/listed-products"

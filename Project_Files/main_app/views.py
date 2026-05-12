from django.shortcuts import render, redirect


from .models import Inquiry, Product, InquiryStatus, CustomUser
from .forms import (
    InquiryForm,
    ProductForm,
    InquiryStatusForm,
    CustomUserCreationForm,
    InquiryUpdate,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    View,
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
        form.instance.item_id = Product.objects.get(pk=self.kwargs.get("pk"))

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

    # def get_context_data(self, **kwargs):
    #     print(self.request.user.inquiries)
    #     return super().get_context_data(**kwargs)


class UploadedProductsList(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    template_name = "home-supplier.html"
    context_object_name = "products"

    # Only return products that belong to the logged-in supplier
    def get_queryset(self):
        return Product.objects.filter(supplier_id=self.request.user)


class DeleteProduct(UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user.role == "Supplier" or self.request.user.is_superuser

    model = Product
    success_url = "/listed-products"


class ShowInquiresView(ListView):
    model = Inquiry
    template_name = "suppliers/customers-inquires.html"
    context_object_name = "inquires"


class ResolveInquiryView(CreateView):
    model = InquiryStatus
    form_class = InquiryStatusForm
    template_name = "suppliers/inquires-status-from.html"
    success_url = "suppliers/customers-inquires"


class CustomerRequestsHistoryView(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.role == "Customer" or self.request.user.is_superuser

    model = Inquiry
    template_name = "customers/requests-history.html"
    context_object_name = "inquiries"


    def get_queryset(self):
        return Inquiry.objects.filter(customer_id=self.request.user)


def toggle_inquiry(request, pk):
    inquiry = Inquiry.objects.get(pk=pk)
    if request.method == "POST":
        form = InquiryUpdate(request.POST, instance=inquiry)
        if form.is_valid():
            form.save()
            return redirect("/suppliers/customers-inquires")
    form = InquiryUpdate(instance=inquiry)
    return render(request, "suppliers/inquires-status-from.html", {"form": form})


# def toggle_inquiry(request, id):
#     pass

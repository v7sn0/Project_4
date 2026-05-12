from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage),
    # Supplier urls
    path("sign-up/", views.SignUpView.as_view()),
    path("suppliers/create", views.UploadProductView.as_view()),
    path("listed-products", views.UploadedProductsList.as_view()),
    path("suppliers/<int:pk>/update", views.UpdateProductView.as_view()),
    path("suppliers/customers-inquires", views.ShowInquiresView.as_view()),
    # path("suppliers/inquiry/<int:pk>", views.ResolveInquiryView.as_view()),
    path("suppliers/inquiry/<int:pk>", views.toggle_inquiry),
    # Customer urls
    path("products/", views.ListProductsView.as_view()),
    path("customers/<int:pk>/create", views.CreateInquiryView.as_view()),  # edited
    path("customers/my-requests", views.CustomerRequestsHistoryView.as_view()),
    path("suppliers/<int:pk>/delete", views.DeleteProduct.as_view()),
]
# hi

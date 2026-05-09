from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage),
    path("sign-up/", views.SignUpView.as_view()),
    path("customers/create", views.CreateInquiryView.as_view()),
    path("suppliers/create", views.UploadProductView.as_view()),
]

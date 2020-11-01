from django.urls import path

from .views import CustomerListView, CustomerDetailView

urlpatterns = [
    path("", CustomerListView.as_view()),
    path("<pk>", CustomerDetailView.as_view()),
]
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from customer.models import Customer
from .serializers import CustomerSerializer


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

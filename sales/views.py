from rest_framework import viewsets
from sales.models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(farm=self.request.user.farm)

    def perform_create(self, serializer):
        serializer.save(farm=self.request.user.farm)
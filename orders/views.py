from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderStatusView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        order = self.get_object()
        processed_status = order.processed_status
        return Response({'processed_status': processed_status})


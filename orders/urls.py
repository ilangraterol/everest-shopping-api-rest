# orders/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, OrderStatusView, OrderUpdateView

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
    path('order-status/', OrderStatusView.as_view(), name='order-status-root'),
    path('orders/<int:id>/update/', OrderUpdateView.as_view(), name='order_update'),
]


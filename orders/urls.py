# orders/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, OrderStatusView

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
]

urlpatterns += router.urls

# Agregamos la siguiente línea para incluir el endpoint de order-status en la raíz de la API
urlpatterns.append(path('order-status/', OrderStatusView.as_view(), name='order-status-root'))

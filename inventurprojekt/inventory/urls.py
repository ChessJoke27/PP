from django.urls import path
from .views import ItemListCreateView, ItemDetailView, OrderListCreateView, OrderDetailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]


from django.urls import path
from .views import (
    ProductListView,
    AddToCartView,
    OrderDetailView,
    PaymentView,
    ProductDetailView,
    AddressListView,
    AddressCreateView,
    AddressUpdateView,
    AddressDeleteView,
    CountryListView,
    OrderItemDeleteView,
    OrderQuantityUpdateView,
    PaymentListView

)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('order-items/<pk>/delete/',
         OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('order-item/update-quantity/',
         OrderQuantityUpdateView.as_view(), name='order-item-update-quantity'),
    path('checkout/', PaymentView.as_view(), name='checkout'),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('addresses/<pk>/update/',
         AddressUpdateView.as_view(), name='address-update'),
    path('addresses/<pk>/delete/',
         AddressDeleteView.as_view(), name='address-delete'),
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),



]

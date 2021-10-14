from django.urls import path, include

from retail_api.views import (
                                ProductListView,
                                StoreListView,
                                StoreDetailView,
                                CustomerListView,
                                CustomerDetailView,
                                OrderListView,
                                OrderDetailView,
                                OrderFullListView,
                                StaffListView,
                                ReviewCreateView,
                                ReviewListView,
                                ReviewDetailView
                            )
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('stores/<int:pk>/staff/', StaffListView.as_view(), name='store-staff-list'),
    path('stores/<int:pk>/orders/', OrderListView.as_view(), name='store-order-list'),
    path('stores/<int:pk>/create-review/', ReviewCreateView.as_view(), name='review-create'),
    path('stores/<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='store-order-detail'),
    path('orders/', OrderFullListView.as_view(), name='full-order-list'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]

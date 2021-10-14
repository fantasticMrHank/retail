from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
# searching
from rest_framework import filters
#  filtering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from retail_api.models import Product, Store, Customer, Order, Order_Item, Staff, Review
from retail_api.permissions import IsReviewer_Staff_ReadOnly
from retail_api.serializers import (ProductSerializer, StoreSerializer, 
                                    CustomerSerializer, OrderSerializer, 
                                    StaffSerializer, ReviewSerializer
                                    )


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class StoreListView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# this is magic too, I don't even need to wire up pk
class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class OrderListView(generics.ListCreateAPIView):    
    serializer_class = OrderSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields =['store__name', 'staff__first_name', 'staff__last_name']
    filterset_fields =['staff__id']
    def get_queryset(self):
        pk = self.kwargs['pk']
        # this is fucking magic
        return Order.objects.filter(store=pk)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderFullListView(generics.ListCreateAPIView):    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields =['store__name', 'staff__first_name', 'staff__last_name']

# get staff list for specific store
class StaffListView(generics.ListCreateAPIView):    
    serializer_class = StaffSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        # this is fucking magic
        return Staff.objects.filter(store=pk)

class ReviewListView(generics.ListAPIView): 
    serializer_class = ReviewSerializer
    
    # I.E. /watchlist/6/reviews?active=false&reviewer__username=tom
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields =['reviewer__username']
    # api/stores/1/reviews/?ordering=-rating
    # ordering_fields =['rating']  ---> this is unnecessary

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(store=pk)

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        current_store = Store.objects.get(pk=pk)

        current_reviewer = self.request.user
        review_queryset = Review.objects.filter(store=current_store, reviewer=current_reviewer)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this store!")

        total_ratings = (current_store.num_reviews * current_store.avg_rating) + serializer.validated_data['rating']
        current_store.num_reviews = current_store.num_reviews + 1 
        current_store.avg_rating = total_ratings / current_store.num_reviews
        current_store.save()
        
        serializer.save(store = current_store, reviewer= current_reviewer)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # this is a PUT, PATCH or DELETE!!!
    permission_classes = (IsReviewer_Staff_ReadOnly,)
        

        
    

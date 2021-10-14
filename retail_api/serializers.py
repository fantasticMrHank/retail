from rest_framework import serializers
from retail_api.models import Product, Store, Staff, Order, Customer, Order_Item, Review

class OrderItemSerializer(serializers.ModelSerializer):
    # display product name instead of id
    product = serializers.CharField(source='product.name')
    # not really helpful
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order_Item
        fields = '__all__'

    def get_total_price(self, obj):
        return float(obj.price) * obj.quantity

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.name')
    class Meta:
        model = Staff
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # customer and staff name instead of id
    served_by = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    # return store name instead of id
    store = serializers.CharField(source='store.name')
    
    order_item = OrderItemSerializer(many=True, read_only = True)
     
    class Meta:
        model = Order
        fields = '__all__'

    def get_served_by(self, object):
        return f'{object.staff.first_name} {object.staff.last_name}'

    def get_customer_name(self, object):
        return f'{object.customer.first_name} {object.customer.last_name}'

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # we are excluding sotre because we are passing the store in from pk in url!!
        exclude = ('store',)
        # fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):

    # when fields are read_only, we don't add them when we create new record
    # we just display them if they are available 
    review = ReviewSerializer(many=True, read_only=True)
    order = OrderSerializer(many=True, read_only = True)
    staff = StaffSerializer(many=True, read_only = True)
    class Meta:
        model = Store
        fields = '__all__'
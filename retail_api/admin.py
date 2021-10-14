from django.contrib import admin

from retail_api.models import Product, Customer, Order, Order_Item, Store, Staff, Review

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order_Item)
admin.site.register(Order)
admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Review)

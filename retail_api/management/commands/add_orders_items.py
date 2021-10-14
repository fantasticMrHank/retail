from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from retail_api.models import Customer, Store, Staff, Order, Order_Item, Product
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('new_items.csv') as file:
            csv_obj = csv.reader(file)

            next(csv_obj)
# order id,product id,price,quantity
            for line in csv_obj:
                print(line)
                this_order = Order.objects.get(id=int(line[0]))
                this_product = Product.objects.get(id=int(line[1]))
                
                
                Order_Item.objects.create( order=this_order, product=this_product, 
                                            price = float(line[2]), quantity=int(line[3])
                )

               
        self.stdout.write("all order items have bee added") 
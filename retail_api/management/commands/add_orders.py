from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from retail_api.models import Customer, Store, Staff, Order
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('orders.csv') as file:
            csv_obj = csv.reader(file)

            next(csv_obj)

            for line in csv_obj:
                from django.core.management.base import BaseCommand
from retail_api.models import Product, Store, Staff
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('orders.csv') as file:
            csv_obj = csv.reader(file)

            next(csv_obj)

            for line in csv_obj:
                
                this_customer = Customer.objects.get(id=int(line[0]))
                this_store = Store.objects.get(id=int(line[1]))
                this_staff = Staff.objects.get(id=int(line[2]))
                
                Order.objects.create( customer=this_customer, 
                                        store=this_store,
                                        staff=this_staff,
                                        order_date =parse_datetime(line[3]))

               
        self.stdout.write("all orders have bee added") 
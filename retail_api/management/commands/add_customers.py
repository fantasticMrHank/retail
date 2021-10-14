from django.core.management.base import BaseCommand
from retail_api.models import Customer, Store
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('customers.csv') as file:
            csv_obj = csv.reader(file)

            # next(csv_obj)

            for line in csv_obj:
                # thisDealer = Dealership.objects.get(name=line[5])
                Customer.objects.create( first_name=line[0], last_name=line[1])
                #print(line)

        self.stdout.write("all customers have bee added") 
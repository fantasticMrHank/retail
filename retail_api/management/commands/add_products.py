from django.core.management.base import BaseCommand
from retail_api.models import Customer, Product
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('products.csv') as file:
            csv_obj = csv.reader(file)

            # next(csv_obj)

            for line in csv_obj:
                # thisDealer = Dealership.objects.get(name=line[5])
                Product.objects.create( name=line[0])
                #print(line)

        self.stdout.write("all products have bee added") 
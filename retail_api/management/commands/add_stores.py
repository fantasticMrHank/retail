from django.core.management.base import BaseCommand
from retail_api.models import Customer, Store
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('stores.csv') as file:
            csv_obj = csv.reader(file)

            next(csv_obj)

            for line in csv_obj:
                # thisDealer = Dealership.objects.get(name=line[5])
                Store.objects.create( name=line[0], street=line[1], city=line[2], state=line[3], zipcode=line[4], phone=line[5])
                #print(line)

        self.stdout.write("all stores have bee added") 
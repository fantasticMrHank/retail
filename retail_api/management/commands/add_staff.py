from django.core.management.base import BaseCommand
from retail_api.models import Product, Store, Staff
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('staff.csv') as file:
            csv_obj = csv.reader(file)

            next(csv_obj)

            for line in csv_obj:
                store_id = int(line[2])
                this_store = Store.objects.get(id=store_id)
                Staff.objects.create( first_name=line[0], last_name=line[1], store=this_store, active=True)

        self.stdout.write("all staff have bee added") 
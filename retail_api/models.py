from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='review')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.rating > 1:
            return f'{self.rating} star for {self.store.name} from {self.reviewer.username}'
        return f'{self.rating} stars for {self.store.name} from {self.reviewer.username}'

class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'customer: {self.first_name} {self.last_name}'

class Store(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=20)

    avg_rating = models.FloatField(default=0)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    store = models.ForeignKey('Store', related_name='staff', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)    

    def __str__(self):
        return f'staf at {self.store.name}, {self.first_name} {self.last_name}'

class Order(models.Model):
    customer= models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='order')
    store = models.ForeignKey('Store', related_name='order', on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='order')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order number: {self.id}'

class Order_Item(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order_item')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order item: {self.id}'





    

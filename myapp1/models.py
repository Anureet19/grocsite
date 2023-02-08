from django.db import models
import datetime

from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)

class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'),]
    fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city=models.CharField(max_length=2, choices=CITY_CHOICES, default='WD')
    interested_in = models.ManyToManyField(Type)

class OrderItem(models.Model):
    STATUS_OF_ORDER = [
        (0,'Cancelled Order'),
        (1,'Placed Order'),
        (2,'Shipped Order'),
        (3,'Delivered Order')
    ]
    item = models.ForeignKey(Item, related_name='orderedItems', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)
    noOfItems = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_OF_ORDER)
    date = models.DateField


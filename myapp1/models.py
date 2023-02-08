from django.core.validators import RegexValidator
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
    description = models.TextField(blank=True)

class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'),]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city=models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

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
    date = models.DateField()


from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Sum
import datetime

from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def topup(self):
        return self.stock + 200
        # self.save()
    def __str__(self):
        return self.name


class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        verbose_name = 'Client'

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    ORDER_STATUS_CHOICES = [
        (0, 'Cancelled Order'),
        (1, 'Placed Order'),
        (2, 'Shipped Order'),
        (3, 'Delivered Order')
    ]
    item = models.ForeignKey(Item, related_name='orderedItems', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='orderedItems', on_delete=models.CASCADE)
    total_items_ordered = models.IntegerField(null=True, default=0)
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=0)
    order_updated_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.client.first_name} ordered {self.total_items_ordered} units of {self.item.name}"

    def total_price(self):
        return self.item.price * self.total_items_ordered


class Description(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    description_given_on = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item

# Create your views here.
def index(request):
    item_list = Item.objects.all().order_by('-price')
    response = HttpResponse()
    heading1 = '<p>' + 'Different Items: ' + '</p>'
    heading2 = '<p>' + 'Item Name' + ': ' + 'Price' + '</p>'
    response.write(heading1)
    response.write(heading2)
    for item in item_list:
        para = '<p>' + str(item) + ': ' + str(item.price) + '</p>'
        response.write(para)
    return response

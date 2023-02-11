from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404

# Create your views here.
def index(request):
    item_list = Item.objects.all().order_by('-price')
    response = HttpResponse()
    heading1 = '<p>' + 'Different Items: ' + '</p>'
    heading2 = '<p>' + 'Item Name' + ': ' + 'Price' + '</p>'
    response.write(heading1)
    response.write(heading2)
    for item in item_list[:10]:
        para = '<p>' + str(item) + ': ' + str(item.price) + '</p>'
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    heading1 = 'This is an Online Grocery Store'
    response.write(heading1)
    return response

def detail(request, type_no= None):
    response = HttpResponse()
    if(type_no):
        item_list = get_list_or_404(Item, type=type_no)
        for item in item_list:
            para = '<p>' + str(item) + '</p>'
            response.write(para)
    return response
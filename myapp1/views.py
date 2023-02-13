from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404
import datetime
from django.shortcuts import render

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

def about(request, year=None, month=None):
    response = HttpResponse()
    heading1 = '<h1>'+'This is an online grocery store'+'</h1>'
    if (year and month):
        datetime_obj = datetime.datetime.strptime(str(month), "%m")
        heading1 = '<h1>'+'This is an online grocery store - ' + datetime_obj.strftime("%B") +' '+ str(year)+'</h1>'
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

def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})
# YES, we are passing an extra context variables to the template i.e a list of all the types
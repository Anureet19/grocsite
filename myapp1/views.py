from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
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
    heading1 = {'heading1':'This is an online grocery store'}
    if (year and month):
        datetime_obj = datetime.datetime.strptime(str(month), "%m")
        heading1 = {'heading1':'This is an online grocery store : '+ datetime_obj.strftime("%B") +' '+ str(year)}
    return render(request,'myapp1/about0.html',heading1)
# YES, passing extra context variable to the template
# passing "heading1" as context to display main heading on the about page

def detail(request, type_no= None):
    if(type_no):
        item_type = str(Type.objects.get(id=type_no))
        item_list = get_list_or_404(Item, type=type_no)
    return render(request,"myapp1/detail0.html",{'item_list':item_list, 'type':item_type})
# YES, we are passing an extra context variables to the template i.e a list of all the items to display on the page

def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})
# YES, we are passing an extra context variables to the template i.e a list of all the types

def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})

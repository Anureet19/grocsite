from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item

# Create your views here.
def index(request):
    type_list = Type.objects.all().order_by('id')
    response = HttpResponse()
    heading1 = '<p>' + 'Different Types: ' + '</p>'
    response.write(heading1)
    for type in type_list:
        para = '<p>' + str(type.id) + ': ' + str(type) + '</p>'
        response.write(para)
    return response

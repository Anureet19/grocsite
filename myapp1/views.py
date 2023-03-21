# Create your views here.
# Import necessary classes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Type, Item, OrderItem
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
import datetime
from django.shortcuts import render
from .forms import OrderItemForm
from .forms import InterestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required()
def about(request, year=None, month=None):
    heading1 = {'heading1': 'This is an online grocery store'}
    if (year and month):
        datetime_obj = datetime.datetime.strptime(str(month), "%m")
        heading1 = {'heading1': 'This is an online grocery store : ' + datetime_obj.strftime("%B") + ' ' + str(year)}
    return render(request, 'myapp1/about0.html', heading1)


# YES, passing extra context variable to the template
# passing "heading1" as context to display main heading on the about page

@login_required()
def detail(request, type_no=None):
    if (type_no):
        item_type = str(Type.objects.get(id=type_no))
        item_list = get_list_or_404(Item, type=type_no)
    return render(request, "myapp1/detail0.html", {'item_list': item_list, 'type': item_type})


# YES, we are passing an extra context variables to the template i.e a list of all the items to display on the page

@login_required()
def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


# YES, we are passing an extra context variables to the template i.e a list of all the types

@login_required()
def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})


@login_required()
def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.total_items_ordered <= order.item.stock:
                order.save()
                order.item.stock -= order.total_items_ordered
                order.item.save()
                msg = 'Your order has been placed successfully.'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})


@login_required()
def itemdetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if not item.available:
        msg = "This item is currently not available."
    else:
        msg = ""
        if request.method == 'POST':
            form = InterestForm(request.POST)
            if form.is_valid():
                item.interested += int(form.cleaned_data['interested'])
                item.save()
                msg = "Your interest in this item has been recorded."
        else:
            form = InterestForm()
    return render(request, 'myapp1/itemdetail.html', {'item': item, 'form': form, 'msg': msg})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp1:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp1/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp1:login')))


@login_required
def myorders(request):
    user = request.user
    if user.is_staff:
        orders = OrderItem.objects.filter(client=user)
        return render(request, 'myapp1/myorders.html', {'orders': orders})
    else:
        message = 'You are not a registered client!'
        return render(request, 'myapp1/myorders.html', {'message': message})

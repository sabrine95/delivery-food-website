from django.shortcuts import render
from django.http import JsonResponse
import json
from . models import *
import datetime
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, Info, LoginForm
from django.contrib.auth import authenticate, login
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from.models import Customer



def home(request):
     products = Product.objects.all()
     context = {'products':products}
     return render(request, 'home/index.html', context)

def about(request):
     context = {}
     return render(request, 'home/about.html', context)

def Restaurants(request):
     restaurants = Restaurant.objects.all()
     context = {'restaurants': restaurants}
     return render(request, 'home/news.html', context)     
def Contact(request):
     context = {}
     return render(request, 'home/contact.html', context) 
def user_Login(request):
      if request.method == "POST":
        forml = LoginForm(data=request.POST)
        if forml.is_valid():
            cd = forml.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('checkout'))
                else:
                    return HttpResponse("failed")
            else:
                return HttpResponse("failed to log")
      else:
        forml = LoginForm()
      return render(request, 'home/loginn.html', {"forml": forml})


def Signup(request):
     if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        form2 = Info(data=request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

        return redirect(reverse('loginn'))
     else:
        form = SignUpForm()
        form2 = Info()
     return render(request, 'home/signup.html', {'form': form, 'form2': form2})
    
def cart(request):
      context = {}
      return render(request, 'home/cart.html', context) 

def Checkout(request):
     # if request.user.is_authenticated:
     #           customer = request.user.customer
     #           order, created = Order.objects.get_or_create(customer=customer, complete=False)
     #           items = order.orderitem_set.all()
     # else:
	# 	#Create empty cart for now for non-logged in user
     #           items = []
     #           order = {'get_cart_total':0, 'get_cart_items':0}
               # context = {'items':items, 'order':order}
               context ={}
               return render(request, 'home/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	# transaction_id = datetime.datetime.now().timestamp()
	# data = json.loads(request.body)

	# if request.user.is_authenticated:
	# 	customer = request.user.customer
	# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	# else:
	# 	customer, order = guestOrder(request, data)

	# total = float(data['form']['total'])
	# order.transaction_id = transaction_id

	# if total == order.get_cart_total:
	# 	order.complete = True
	# order.save()

	# if order.shipping == True:
	# 	ShippingAddress.objects.create(
	# 	customer=customer,
	# 	order=order,
	# 	address=data['shipping']['address'],
	# 	city=data['shipping']['city'],
	# 	state=data['shipping']['state'],
	# 	zipcode=data['shipping']['zipcode'],
	# 	)

	return JsonResponse('Payment submitted..', safe=False)

def Singleitem(request):
     context = {}
     return render(request, 'home/single-news.html', context)                                

# def cart(request):
#      context = {}
#      return render(request, 'store/cart.html', context)

# def checkout(request):
#       context = {}
#       return render(request, 'store/checkout.html', context)
# Create your views here.

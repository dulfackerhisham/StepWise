from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Order,OrderItem
from carts.models import Cart
from products.models import ProductItem
from django.contrib import messages
from accounts.models import Profile
from . constants import PAYMENT_TYPE_RAZORPAY


import random

# Create your views here.

# TODO: transaction.atomic
@login_required(login_url='logIn')
def place_order(request):
    """
    docstrings 
    """
    if request.method == 'POST':
        neworder = Order()
        neworder.user = request.user
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        # TODO: FORM VALIDATION
        # Check if a Profile for the user exists, and create/update it
        address, created= Profile.objects.get_or_create(user=request.user)

        address.user = request.user
        address.fname = request.POST.get('fname')
        address.lname = request.POST.get('lname')
        address.phone = request.POST.get('phone')
        address.email = request.POST.get('email')
        address.country = request.POST.get('country')
        address.address = request.POST.get('address')
        address.city = request.POST.get('city')
        address.state = request.POST.get('state')
        address.pincode = request.POST.get('pincode')
        address.save()

        neworder.address = address

        
        subtotal = 0
        cart = Cart.objects.filter(user=request.user)
        # TODO : remove for loop move to DB
        for item in cart:
            ttlprice = item.product.price * item.qty
            subtotal += ttlprice

        neworder.total_price = subtotal

        # TODO: separate this in another function without use of while loop
        tracking_number = f"{request.user.username}-{random.randint(1111111,9999999)}"
        
        #verifying if tracking number is already existing or not
        while Order.objects.filter(tracking_no=tracking_number).exists():
            # TODO: remove while loop
            tracking_number = f"{request.user.username}-{random.randint(1111111,9999999)}"

        neworder.tracking_no = tracking_number
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            #bulk (create) update
            totalprice = item.product.price * item.qty

            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.price,
                quantity = item.qty,
                total_amount = totalprice,
                # TODO: remove total aount
            )

            #decreasing product quantity from available stock
            # TODO: locking mechanism => reduce & bd locker
            orderproduct = ProductItem.objects.filter(id=item.product.id).first()
            orderproduct.stock = orderproduct.stock - item.qty
            orderproduct.save()


        #clearing user's cart
        Cart.objects.filter(user=request.user).delete()


        pay_mode = request.POST.get('payment_mode')
        if (pay_mode == PAYMENT_TYPE_RAZORPAY):
            # TODO: translation languages
            return JsonResponse({'status': "Your Order has been placed successfully"})
        else:
            messages.success(request, "Your Order has been placed successfully")

    return redirect("/")

@login_required(login_url='logIn')
def razorpay_check(request):
    cart = Cart.objects.filter(user=request.user)
        # TODO : remove for loop move to DB

    subtotal = 0
    for item in cart:
        totalprice = item.product.price * item.qty
        subtotal += totalprice

    return JsonResponse({'subtotal': subtotal})

def payment_completed(request):
    return HttpResponse("My Orders Page")

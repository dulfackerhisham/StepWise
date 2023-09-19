from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Cart
from accounts.models import Profile
from django.contrib import messages



@login_required(login_url='logIn')
def checkout_view(request):
    subtotal = 0

    cart = Cart.objects.filter(user=request.user.id)
    for item in cart:
        item.total_price = item.product.price * item.qty
        subtotal += item.total_price

    try:
        active_address = Profile.objects.get(user=request.user, status=True)
    except:
        messages.warning(request, "There are multiple addresses, only one should be Activated.")
        active_address = None
    

    context = {
        'cart': cart,
        'subtotal': subtotal,
        'active_address': active_address,
    }
    return render(request, "checkout.html", context)
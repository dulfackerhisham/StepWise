from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Cart




def checkout_view(request):
    subtotal = 0

    cart = Cart.objects.filter(user=request.user.id)
    for item in cart:
        item.total_price = item.product.price * item.qty
        subtotal += item.total_price

    context = {
        'cart': cart,
        'subtotal': subtotal,
    }
    return render(request, "checkout.html", context)
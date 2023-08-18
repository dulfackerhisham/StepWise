from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect

from . models import Cart
from products.models import ProductItem

# Create your views here.

def addtocart(request):
    # cart_product = {}

    # #current product id
    # cart_product[str(request.GET['id'])] = {
    #     'title': request.GET['title'],
    #     'qty': request.GET['qty'],
    #     'price': request.GET['price']
    # }

    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('id'))

            # Get the ProductItem instance or return 404 if not found
            product_item = get_object_or_404(ProductItem, id=prod_id)

            #at first we are checking if there is product exist with this id
            product_check = ProductItem.objects.get(id=prod_id)
            if (product_check):
                #if user have already added product to cart
                if (Cart.objects.filter(user=request.user.id, product=prod_id)):
                    return JsonResponse({'status': "Product Already in Cart"})
                else:
                    #if product is not in cart we will add product to cart
                    prod_qty = int(request.POST.get('qty'))

                    #reverse the logic
                    if product_check.stock >= prod_qty:
                        Cart.objects.create(user=request.user, product=product_item, qty=prod_qty, is_paid=False)
                        return JsonResponse({'status': "Product Added Successfully"})
                    else:
                        return JsonResponse({'status': "Only" +str(product_check.stock) + " Quantity Available"})

            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect('/')

    # return render(request, "cart.html")


def viewcart(request):
    cart = Cart.objects.filter(user=request.user.id).order_by('-createdDate')

    for item in cart:
        item.total_price = item.product.price * item.qty

    context = {'cart': cart}

    return render(request, "cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('id'))
        prod_qty = int(request.POST.get('qty'))

        if Cart.objects.filter(user=request.user, product=prod_id).exists():
            cart = Cart.objects.get(product=prod_id, user=request.user)
            p_stock = cart.product.stock
            
            if p_stock < prod_qty:
                return JsonResponse({'status': "Product Only Have " + str(p_stock) + " Stocks"}) #cant see the error
            else:
                print(prod_qty)
                cart.qty = prod_qty
                cart.save()
                #here delete a quantity based on adding the quantity
                return JsonResponse({'status': "Updated Successfully"})
        else:
            return JsonResponse({'status': "Product not found in cart"})

    return redirect('/')



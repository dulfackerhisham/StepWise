from django.shortcuts import render

# Create your views here.

def add_to_cart(request):
    cart_product = {}

    #current product id
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price']
    }

    #checking if there is cart data in current session
      

    return render(request, "cart.html")

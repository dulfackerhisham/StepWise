from django.urls import path
from .views import addtocart, viewcart, updatecart, deletecart

urlpatterns = [
    path("add_to_cart/", addtocart, name='add_to_cart'),
    path("cart/", viewcart, name='cart'),
    path("update-cart/", updatecart, name='updatecart'),
    path("delete-cart/", deletecart, name='deletecart'),
    
]


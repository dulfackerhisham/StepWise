from django.urls import path
from . views import place_order, razorpay_check, payment_completed

urlpatterns = [
    path("", place_order, name="placeorder"),

    # razorpay
    path("proceed-to-pay/", razorpay_check, name="proceed-to-pay"),
    path("payment-completed/", payment_completed, name="payment-completed"),
]
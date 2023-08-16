from django.urls import path
from .views import sign_up, log_in, log_out, otp_verification , resend_otp

urlpatterns = [
    path('', log_in, name="logIn"),
    path('signup/', sign_up, name="signup"),
    path('otpVerify/', otp_verification, name="otp_verification"),
    path('resend_otp/', resend_otp, name="resend_otp"),
    path('logout/', log_out, name="logout"),
]
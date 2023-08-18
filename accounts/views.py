from django.shortcuts import redirect, render
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse

from django.conf import settings
import random
from django.core.cache import cache
from django.core.mail import send_mail

# from django.views.decorators.cache import cache_control



# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        # username = requset.POST.get('username')
        username  = request.POST['username']
        email     = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #credentials are saving in session
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password1



        #validation for signup
        if username.strip() == '' or email.strip() == '' or password1.strip() == '' or password2.strip() == '':
            messages.error(request, "All fields are required")
            return render(request, "signup.html")
        
        if len(password1) < 8 or len(password2) < 8:
            messages.error(request, "Password must have 8 characters!")
            return render(request, "signup.html")
        
        
        if password1 == password2:
            if len(username) > 15:
                messages.error(request, "Username must be under 15 characters!")
                return render(request, "signup.html")
            elif Account.objects.filter(username=username).exists():
                messages.error(request, "Username already exists! Please try some other username")
                return render(request, "signup.html")
            elif not username.isalnum():
                messages.error(request, "Username must be in Alpha-numeric!")
                return render(request, "signup.html")
            elif Account.objects.filter(email=email).exists():
                messages.error(request, "Email already in use! Please try some other email")
                return render(request, "signup.html")
            else:
                #generating otp & saves in session
                random_otp = str(random.randint(0000, 9999))
                cache.set('generated_otp', random_otp, 30)
                print(random_otp)
                #sending email
                subject = "Welcome to StepWise !!!"
                message = (f"""Hello {username}
                           Your otp is generated
                           {random_otp}""")
        
                to_list = [email]
                send_mail(subject, message, settings.EMAIL_HOST_USER, to_list, fail_silently=False)
                return redirect('otp_verification')
        else:
            messages.error(request, "Password is not matching!")
            return render(request, "signup.html")

        #creating user object
        # user = Account.objects.create_user(
        #     username = username, email = email, password = password1)
        # user.save()


    return render(request, "signup.html")


def otp_verification(request):

    if request.method == 'POST':
        submitted_otp = request.POST.get('submitted_otp')
        generated_otp = cache.get('generated_otp')
        print(submitted_otp)

        if submitted_otp == generated_otp:
            user = Account.objects.create_user(
                username=request.session['username'],
                email=request.session['email'],
                password=request.session['password']
            )
            user.is_active = True
            user.save()

            # Clear the cache after successful verification
            cache.delete('generated_otp')

            messages.success(request, "Your account has been successfully created.")
            return redirect('logIn')
        else:
            messages.error(request, "OTP doesn't match or has expired.")
            return redirect('otp_verification')


    # Handle the case where the request method is not POST (GET, etc.)
    return render(request, "otp.html")
    


def resend_otp(request):
    if request.method == 'GET':
        email = request.session.get('email')
        username = request.session.get('username')

        # Generating new OTP
        random_otp = str(random.randint(0000, 9999))
        cache.set('generated_otp', random_otp, 30)
        print(random_otp)

        # Sending email
        subject = "Resend OTP - StepWise !!!"
        message = (f"""Hello {username}
                   Your New OTP is generated
                   {random_otp}""")
        
        to_list = [email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, to_list, fail_silently=False)
        messages.success(request, "New OTP has been sent to your email")    

    # Redirect the user back to the OTP verification page
    return redirect('otp_verification')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']

        user = authenticate(email=email, password=password1)

        if user is not None:
            #this is not enough
            if user.is_superuser:
                messages.error(request, "Admin Is Not Allowed To Log in User Side")
                return redirect('logIn')
            else:
                login(request, user)
                # username = user.username
                # messages.success(request, "Logged in successfully")
                return redirect('home')  #try to pop a successfull message when logged in with username
        else:
            messages.error(request, "invalid credentials")
            return redirect('logIn')

    return render(request, "login.html")


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('logIn')
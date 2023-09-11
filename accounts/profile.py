from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required




@login_required(login_url='logIn')
def user_profile(request):
    return render(request, "myAccount.html")
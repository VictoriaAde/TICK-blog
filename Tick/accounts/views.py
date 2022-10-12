from pickle import FALSE
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
import django
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages



def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:home",)
        else:
            messages.error("Invalid your login")
            # Return an 'invalid login' error message.
            return redirect("accounts:signin")

    return render(request, "registrations/login.html")

def Register(request):
    if request.method == "POST":
        input = request.POST
        
        try:
            password2=input["password2"],
            user = User.objects.create_user(
                username=input["username"],
                email=input["email"],
                password=input["password"],
                
                first_name=input["first_name"],
                last_name=input["last_name"],
            )
            
            user.save()
            login(request, user)
        except django.db.utils.IntegrityError:
             
            return render(
                request, "registrations/signUp.html", {"msg": "user already exists"}
            )

        return redirect("main:home")

    return render(request, "registrations/signUp.html",{'register':UserRegistrationForm})

def user_logout(request):
    logout(request)
    messages.info(request, "you have successfully logout")
    return redirect('main:home')
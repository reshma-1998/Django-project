from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def login_page (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter (username = username) . exists():
            messages.error(request, "Invalid username")
            return redirect("login")
        user = authenticate(username=username , password= password)
        if user is None:
            messages.error(request,"Invilid Password")
            return redirect("login")
        else:
            login(request,user)
            return redirect("receipe")
    return render (request, "login.html")

def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_desc=receipe_desc
        )
        return redirect('receipe')
    Queryset = Receipe.objects.all()
    return render(request, "receipe.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username= username)

        if user.exists():
            messages.info(request,"user name already taken")
            return redirect('register')
        user = User.objects.create(
            first_name= first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Succefully")
        return redirect("register")
    return render(request, "register.html")
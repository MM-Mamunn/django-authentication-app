from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "in.html")
    return HttpResponse("HI")
    
def signup(request):
    return render(request, "signin.html")
def signup2(request):

    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Signup successfull")
        
        return redirect('home')
    else:
        return render(request, "signin.html")
def logoutmain(request):
    logout(request)
    return redirect('home')
def loginmain(request):
        return render(request, "login.html")
def login2(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            # return HttpResponse("logged in")
            return redirect('home')
        else:
            messages.error(request,"error")
            return redirect("home")
    else:
        return render(request, "login.html")

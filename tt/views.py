from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from st.models import students
from .models import teachers
# Create your views here.
def tsignup(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')

        idd=request.POST.get('idd')
        dept=request.POST.get('dept')
        password=request.POST.get('password')
        username=request.POST.get('username')
        username = 'tt'+username
        myuser= User.objects.create_user(username,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        nt = teachers(fullname=f'{fname} {lname}' ,username =username,password = password,teachers_id=idd,department=dept)
        nt.save()
        # else
        messages.success(request,"Signup successfull")
        
        return redirect('home')
    else:
        return HttpResponse("hi")
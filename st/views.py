from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import students
from tt.models import teachers

# Create your views here.
def home(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'st' in request.user.username:
            dic={'data':'error'}
            stdata =students.objects.all()
            for i in stdata:
                # if authenticate(request,username=i.username,password=i.password): 
                if i.username == request.user.username:
                    dic={
                        'data':i,
                    }
                return render(request, "home.html",dic)
            
        else :
            return render(request, "thome.html")
    else:
        # return HttpResponse("HI")
        return render(request, "in.html")
    
def signupts(request):
    return render(request, "signints.html")   
def signup(request):
    return render(request, "signin.html")
def signup2(request):

    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        advisor=request.POST.get('advisor')
        username = 'st'+username
        
        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        ns = students(name=f'{fname} {lname}' ,username =username,password = password,advisor=advisor)
        ns.save()
        # else
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
        username2 = username
        username2='tt'+username2
        username = 'st'+username
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            # using redirect to activate '/' url to hover on profile
            # return redirect('home')
            return HttpResponseRedirect('/')
        user2 = authenticate(request,username=username2,password=password)
        if user2 is not None:
            login(request, user2)
            # using redirect to activate '/' url to hover on profile
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("hlw {{username2}} {{password}}")

            messages.error(request,"error")
            return redirect("home")
    else:
        return render(request, "login.html")

def advisor(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'st' in request.user.username:
            dic={'data':'none'}
            stdata =students.objects.all()
            for i in stdata:
                # if authenticate(request,username=i.username,password=i.password): 
                if i.username == request.user.username:
                    # return HttpResponse("hlo")
                    a = 'tt'+i.advisor
                    ttdata=teachers.objects.filter(user_name__icontains=a)
                    dic={
                        'data':ttdata,
                    }
            return render(request, "advisor.html",dic)
        else:
            return redirect('home')
    else:
        return redirect('home')




def tsignup2(request):
    return render(request, "tsignin.html")
def tsignup(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')

        idd=request.POST.get('idd')
        dept=request.POST.get('dept')
        password=request.POST.get('password')
        username=request.POST.get('username')
        username = 'tt'+username
        # username,email,and pass needed minimum
        myuser= User.objects.create_user(username,'mm@gmail.com',password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        nt = teachers(fullname=f'{fname} {lname}' ,user_name =username,password = password,teachers_id=idd,department=dept)
        nt.save()
        # else
        messages.success(request,"Signup successfull")
        
        return redirect('home')
    else:
        return HttpResponse("hi")
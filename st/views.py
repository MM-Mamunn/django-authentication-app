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
            
            # i =students.objects.filter(username__icontains=request.user.username);
            stdata=students.objects.all()
            for i in stdata:
                print(i.username)
                # if authenticate(request,username=i.username,password=i.password): 
                if i.username == request.user.username:
                    print('yes')
                    dic={
                        'data':i,
                        }
            return render(request, "home.html",dic)
            
        elif 'tt' in request.user.username:            
            # i =students.objects.filter(username__icontains=request.user.username);
            ttdata=teachers.objects.all()
            for i in ttdata:
                print(i.user_name)
                # if authenticate(request,username=i.username,password=i.password): 
                if i.user_name == request.user.username:
                    print('yes')
                    dic={
                        'data':i,
                        }
            return render(request, "teacher/thome.html",dic)
        else:
            return HttpResponse("error")
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
        
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
def logoutmain(request):
    logout(request)
    return redirect('loginmain')
def loginmain(request):
        logout(request)
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
        
    return HttpResponseRedirect('/')

def advisor(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'st' in request.user.username:
            dic={'data':''}
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
        
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def allstudent(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            dic={'data':'error'}         
            
            # i =students.objects.filter(username__icontains=request.user.username);
            stdata=students.objects.all()
            l=[]
            for i in stdata:
                t = 'tt'+i.advisor
                # if authenticate(request,username=i.username,password=i.password): 
                if t == request.user.username:
                    l.append(i)
            
            dic={
                        'data':l,
                        }
            return render(request, "teacher/allstudent.html",dic)
        else:
            return redirect('home')
    
    else:
            return redirect('home')



def searchstudent(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            return render(request, 'teacher/searchstudent.html')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

def searchstudent2(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            dic={'data':'error'}
            if request.method == 'POST':
                name=request.POST.get('name')
                data= students.objects.filter(name__icontains=name)
                dic={'data':data}
                return render(request, 'teacher/showstudent.html',dic)
            else:
                return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')
    
def DELETE(request, id):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            dic={'n':0}
            if request.method == 'POST':
                st=students.objects.get(pk=id)
                st2=User.objects.get(username=st.username)
                st.delete()
                st2.delete()
                return render(request,'teacher/success.html',{'n':1})       
            else:
                return render(request,'teacher/success.html',dic)

    return HttpResponseRedirect('/')

def EDIT(request,id):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            st=students.objects.get(pk=id)
            dic={'uid':id,
                'st':st}
            return render(request,'teacher/EDIT.html',dic)
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def EDIT2(request,uid):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            roll=request.POST.get('roll')
            cgpa=request.POST.get('cgpa')
            advisor=request.POST.get('advisor')
            st=students.objects.get(pk=uid)
            if roll is not '':
                st.roll=roll
            if cgpa is not '':
                st.cgpa=cgpa
            if advisor is not '':
                st.advisor=advisor
            st.save()
            return render(request,'teacher/success.html',{'n':1}) 
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')
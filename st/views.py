from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import students
from st.models import teachers
import re

def cgpa_add(request,id,li,n):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            cnt=0
            st=students.objects.get(pk=id)
            li2=[]
            li2.append((st.cgpa1))
            li2.append((st.cgpa2))
            li2.append((st.cgpa3))
            li2.append((st.cgpa4))
            li2.append((st.cgpa5))
            li2.append((st.cgpa6))
            li2.append((st.cgpa7))
            li2.append((st.cgpa8))
            for i in li2:
                if (i) != -1.0:
                    cnt+=1
            # f = 0
            # print(f' li is {li}')
            # for i in range(0,cnt):
            #     if li[i] == -1:
            #         f = 1
            #         break
            print(f'li2 {li2[n-1]}')
            if li2[n-1] == -1.0:
                if (cnt+1) is not n :
                    print(f'cnt is{cnt}')
                    print("error")
                    no=1
                    # return render(request,'teacher/success.html',{'n':1})
                    return no
            print("add_result")
            print(li)
            if(n == 1):
                st.cgpa1=li[0]
            if(n == 2):
                st.cgpa2=li[1]
            if(n == 3):
                st.cgpa3=li[2]
            if(n == 4):    
                st.cgpa4=li[3]
            if(n == 5):   
                st.cgpa5=li[4]
            if(n == 6):
                st.cgpa6=li[5]
            if(n == 7):
                st.cgpa7=li[6]
            if(n == 8):
                st.cgpa8=li[7]
            st.save()
            st=students.objects.get(pk=id)
            
            """calculating semester"""
            semester =1
            t_cg=0
            if st.cgpa1 != -1:
                t_cg+=float(st.cgpa1)
                semester += 1
            if st.cgpa2 != -1:
                t_cg+=float(st.cgpa2)
                semester += 1
            if st.cgpa3 != -1:
                t_cg+=float(st.cgpa3)
                semester += 1
            if st.cgpa4 != -1:
                t_cg+=float(st.cgpa4)
                semester += 1
            if st.cgpa5 != -1:
                t_cg+=float(st.cgpa5)
                semester += 1
            if st.cgpa6 != -1:
                t_cg+=float(st.cgpa6)
                semester += 1
            if st.cgpa7 != -1:
                t_cg+=float(st.cgpa7)
                semester += 1
            if st.cgpa8 != -1:
                t_cg+=float(st.cgpa8)
                semester += 1
            st.sem=semester
            semester -=1
            st.cgpa = (t_cg/(semester))
            st.save()
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

            


                

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
    ttdata=teachers.objects.all()
    dic={
        'tt':ttdata
    }
    return render(request, "signin.html",dic)
def signup2(request):

    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        advisor=request.POST.get('advisor')
        advisor= re.sub(r'.','',advisor,count=2)
        username = 'st'+username
        
        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        ns = students(name=f'{fname} {lname}' ,username =username,password = password,advisor=advisor)
        ns.save()
        # else
        return render(request,'teacher/success.html',{'n':1}) 
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
        return render(request,'teacher/success.html',{'n':0}) 

        
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
        return render(request,'teacher/success.html',{'n':1}) 
        
    else:
        return render(request,'teacher/success.html',{'n':0}) 
    
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
                data= students.objects.filter(name__iexact=name)
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
            tt=teachers.objects.all()
            dic={'uid':id,
                'st':st,
                'tt':tt}
            

            
            return render(request,'teacher/EDIT.html',dic)
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def EDIT2(request,uid):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            roll=request.POST.get('roll')
            advisor=request.POST.get('advisor')
            advisor= re.sub(r'.','',advisor,count=2)
            st=students.objects.get(pk=uid)
            if roll is not '':
                st.roll=roll
            if advisor is not '':
                st.advisor=advisor
            st.save()
            return render(request,'teacher/success.html',{'n':1}) 
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


def result(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:

            stdata =students.objects.all()
            l=[]
            for i in stdata:
                t = 'tt'+i.advisor
                # if authenticate(request,username=i.username,password=i.password): 
                if t == request.user.username:
                    l.append(i)
            
            dic={
                'stdata':l
            }
            return render(request,'teacher/result.html',dic)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def result2(request,id):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
                st=students.objects.get(pk=id)
                dic={
                    'id':id,
                    'st':st,
                }
                return render(request,'teacher/result2.html',dic)
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')
def result3(request,id):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            if request.method == 'POST':
                cgpa1=(request.POST.get('cgpa1'))
                cgpa2=(request.POST.get('cgpa2'))
                cgpa3=(request.POST.get('cgpa3'))
                cgpa4=(request.POST.get('cgpa4'))
                cgpa5=(request.POST.get('cgpa5'))
                cgpa6=(request.POST.get('cgpa6'))
                cgpa7=(request.POST.get('cgpa7'))
                cgpa8=(request.POST.get('cgpa8'))
                li=[]
                li.append((cgpa1))
                li.append((cgpa2))
                li.append((cgpa3))
                li.append((cgpa4))
                li.append((cgpa5))
                li.append((cgpa6))
                li.append((cgpa7))
                li.append((cgpa8))
                n=1
                for i in range(0,8):
                    if (li[i] != ''):
                        n=i+1
                        break
                # print(id)
                # print(li)
                # print(n)
                no =cgpa_add(request,id,li,n)
                if no == 1:
                    return render(request,'teacher/success.html',{'n':0})
                else:
                    return render(request,'teacher/success.html',{'n':1})
            else:
                return render(request,'teacher/result2.html',dic={'id':id})
        

        return HttpResponseRedirect('/')
    

    else:
        return HttpResponseRedirect('/')
    
def sresult(request):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'st' in request.user.username:
            stdata=students.objects.all()
            for i in stdata:
                if(i.username == request.user.username):
                    dic={
                        'st':i
                    }
                    return render(request,'sresult.html',dic)
                else:
                    pass
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def sresult2(request,uid):
    if not request.user.is_superuser and request.user.is_authenticated:
        if 'tt' in request.user.username:
            st=students.objects.get(pk=uid)
            dic={
                'id':uid,
                'st':st,
            }
            return render(request,'teacher/result2.html',dic)
        
    return HttpResponseRedirect('/')


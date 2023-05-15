from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

# path('',include('tt.urls')),
path('', views.home,name="home"),
path('signup/',views.signup,name="signup"),
path('signup2/',views.signup2,name="signup2"),
path('loginmain/',views.loginmain,name="loginmain"),
path('login2/',views.login2,name="login2"),
path('logoutmain/',views.logoutmain,name="logoutmain"),
path('tsignup/',views.tsignup,name="tsignup"),
path('tsignup2/',views.tsignup2,name="tsignup2"),
path('signupts/',views.signupts,name="signupts"),
path('advisor/',views.advisor,name="advisor"),
path('allstudent/',views.allstudent,name="allstudent"),
path('searchstudent/',views.searchstudent,name="searchstudent"),
path('searchstudent2/',views.searchstudent2,name="searchstudent2"),
path('DELETE/<int:id>',views.DELETE,name="DELETE"),
path('EDIT/<int:id>',views.EDIT,name="EDIT"),
path('EDIT2/<int:uid>',views.EDIT2,name="EDIT2"),

# path("login/", include("django.contrib.auth.urls")),
]

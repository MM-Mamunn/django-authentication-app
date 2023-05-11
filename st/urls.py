from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('', views.home,name="home"),
path('signup/',views.signup,name="signup"),
path('signup2/',views.signup2,name="signup2"),
path('loginmain/',views.loginmain,name="loginmain"),
path('login2/',views.login2,name="login2"),
path('logoutmain/',views.logoutmain,name="logoutmain"),
# path("login/", include("django.contrib.auth.urls")),
]

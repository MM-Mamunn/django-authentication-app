from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

# path("login/", include("django.contrib.auth.urls")),
path('',include('st.urls')),
path('tsignup/',views.tsignup,name="tsignup"),
]


from django.urls import path

from authapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
     path('login',views.login,name="login"),
]
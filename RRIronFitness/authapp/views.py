from django.shortcuts import redirect
from django.contrib.auth.models import User,auth

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def signin(request):
    if request.method=='POST':
        firstName=request.POST['fname']
        lastName=request.POST['lname']
        userName=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pwd']

        user=User.objects.create_user(
            username=userName,
            email=email,
            password=password,
            first_name=firstName,
            last_name=lastName)
        return redirect('/')
    else:
        return render(request,'signin.html')    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('your loggedin')
            return redirect('/')
    else:        
       return render(request,'login.html')      
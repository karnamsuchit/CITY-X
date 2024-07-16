from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect, get_object_or_404
from .models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, logout 
from django.http import HttpRequest, HttpResponse
from django.contrib import messages,messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm

from datetime import datetime
# Create your views here.

def home(request):
    return render(request,'home.html')


def guide_details(request, id):
    reg_Guide = get_object_or_404(Reg_Guide, pk=id)
   
    return render(request,'booking/guide_details.html',{'reg_Guide':reg_Guide})

    


def booking(request):
    reg_Guide = Reg_Guide.objects.all()
    context = {'reg_Guide':reg_Guide}
    return render(request, 'booking/booking.html', context)

def guide_register(request):
    if request.method =='POST':
        aadhar_num =  request.POST['aadhar_num'] 
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        place_loc = request.POST['place_loc']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number'] 
        gender = request.POST['gender']
        price = request.POST['price']
        age = request.POST['age'] 
        experience_years = request.POST['experience_years']
        certificate = request.POST['certificate']
        photo = request.POST['photo']
        ins = Reg_Guide(aadhar_num=aadhar_num, name=name, email=email, description=description, date_of_birth=date_of_birth, phone_number=phone_number, gender=gender, age=age, experience_years=experience_years, certificate=certificate,photo=photo, place_loc=place_loc, price=price )
        ins.save()
        return redirect("/booking")

    return render(request, 'booking/guide_register.html')
def bengaluru(request):
    return render(request, 'bengaluru.html')
def mysuru(request):
    return render(request, 'mysuru.html')








def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password )

        if user is not None:
            auth.login(request, user)
            return redirect('home')  # Redirect to desired page after login
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('/')

    return render(request, 'user_auth/login.html')
  
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists.')
                return redirect('signup')

            elif len(password) < 6:
                messages.error(request, 'Password must be at least 6 characters long.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful.')
                return redirect('login')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup') 
 
    else:
        return render(request, 'user_auth/signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

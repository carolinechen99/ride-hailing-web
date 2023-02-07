from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Import models
from .models import Account
# import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# import reverse
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('account:register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('pages:index')
                    user.save()
                    # Create an account for the user
                    # t1 = User.objects.get(username=username)
                    account = Account.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    account.save()


                    
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('account:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('account:register')
    else:
        return render(request, 'account/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('ride:request_ride')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('account:login')
    else:
        return render(request, 'account/login.html')

def logout(request):
    # Check if the user is logged in
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')

def profile(request):
    return render(request, 'account/profile.html')

def driver_register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            #get the user account (invalid account already checked at driver function)
            account = Account.objects.get(username=request.user.username)
            #check if the user is already a driver
            if account.is_driver:
                messages.error(request, 'You are already registered as a driver')
                return redirect('index')
            else:
                return render(request, 'account/driver_register.html')
        else:
            messages.error(request, 'You must be logged in to register as a driver')
            return redirect('account:login')



    if request.method == 'POST':
        # Get form values
        phone = request.POST.get('phone')
        vehicle_plate = request.POST.get('vehicle_plate')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_seats = request.POST.get('vehicle_seats')
        driver_license = request.POST.get('driver_license')

        # Get the user
        d_account = Account.objects.get(username=request.user.username)
        # Check if phone number is already in use
        if Account.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number is already in use')
            return redirect('account:driver_register')
        else:
            # Check if vehicle plate is already in use
            if Account.objects.filter(vehicle_plate=vehicle_plate).exists():
                messages.error(request, 'Vehicle plate is already in use')
                return redirect('account:driver_register')
            else: 
                # Check if driver license is already in use
                if Account.objects.filter(driver_license=driver_license).exists():
                    messages.error(request, 'Driver license is already in use')
                    return redirect('account:driver_register')
                else:
                    # Looks good
                    d_account.phone = phone
                    d_account.vehicle_plate = vehicle_plate
                    d_account.vehicle_type = vehicle_type
                    d_account.vehicle_seats = vehicle_seats
                    d_account.driver_license = driver_license
                    d_account.is_driver = True
                    d_account.save()
                    messages.success(request, 'You are now registered as a driver')
                    return redirect('ride:driver')
    else:
        return render(request, 'account/driver_register.html')


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
    # Check if the user is logged in, if not redirect to login page
    if request.method == 'POST':
        # Get form values
        phone = request.POST.get('phone')
        vehicle_plate = request.POST.get('vehicle_plate')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_seats = request.POST.get('vehicle_seats')
        driver_license = request.POST.get('driver_license')
        # Check if the is_driver field is already true
        if Account.objects.filter(username=request.user.username).values('is_driver')[0]['is_driver'] == True:
            messages.error(request, 'You are already registered as a driver')
            return redirect('index')
        else:
            # Check if vehicle plate is unique 
            if Account.objects.filter(vehicle_plate=vehicle_plate).exists():
                messages.error(request, 'That vehicle plate is taken')
                return redirect('account:driver_register')
            else:
                # Check if driver_license is unique 
                if Account.objects.filter(driver_license=driver_license).exists():
                    messages.error(request, 'That driver_license is taken')
                    return redirect('account:driver_register')
                else:
                    # All good
                    # Add all the information to the corresponding user in the Account table
                    account = Account.objects.get(username=request.user.username)
                    account.phone = phone
                    account.vehicle_plate = vehicle_plate
                    account.vehicle_type = vehicle_type
                    account.vehicle_seats = vehicle_seats
                    account.driver_license = driver_license
                    account.is_driver = True
                    account.save()
                    messages.success(request, 'Successfully registered as a driver')
                    return redirect('index')
    else:
        return redirect('account:login')

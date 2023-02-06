from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import Account

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if Account.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if Account.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    if Account.objects.filter(phone_number=phone_number).exists():
                        messages.error(request, 'That phone number is being used')
                        return redirect('register')
                    else:
                        # Looks good
                        user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, phone_number=phone_number, password=password)
                        # Login after register
                        # auth.login(request, user)
                        # messages.success(request, 'You are now logged in')
                        # return redirect('index')
                        user.save()
                        messages.success(request, 'Successfully registered, now ready to login')
                        return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
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
            return redirect('request_ride')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')

def profile(request):
    return render(request, 'account/profile.html')

def driver_register(request):
    return render(request, 'account/driver_register.html')
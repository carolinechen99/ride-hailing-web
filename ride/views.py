from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse
# Import models
from .models import Ride
from account.models import Account
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/account/login')
def request_ride(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'ride/request_ride.html')
        else:
            messages.error(request, 'You must be logged in to request a ride')
            return redirect('account:login')


    if request.method == 'POST':
        destination = request.POST.get('destination')
        pickup_location = request.POST.get('pickup-loc')
        arr_time = request.POST.get('arr-time')
        party_size = request.POST.get('party-size')
        allow_sharing = request.POST.get('allow-sharing') == 'allow'
        car_type = request.POST.get('car-type')
        special = request.POST.get('special')


        # owner = get_object_or_404(User, pk=request.user.id)
        try:
            owner = User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            messages.error(request, 'You are not logged in')
            return redirect('account:login')
        r = Ride(owner = owner, owner_party_size = party_size, required_arrival_time = arr_time, pickup_location = pickup_location, destination = destination, allow_sharing = allow_sharing,  special_requirements = special)
        r.save()
        messages.success(request, 'Your ride request has been submitted')
        return render(request, 'ride/request_ride.html')
    else:
        return redirect('account:login')


def driver(request):
    if request.method == 'GET':
    # If the User has logged in, direct to driver page
        if request.user.is_authenticated:
            # Check if the user account is valid
            try:
                account = Account.objects.get(username=request.user.username)
            except Account.DoesNotExist:
                messages.error(request, 'User does not exist')
                return redirect('account:login')
            # Check if the user is a driver
            if account.is_driver:
                return render(request, 'ride/driver.html')
            else:
                return redirect('account:driver_register')
        else:
            messages.error(request, 'You must be logged in to view this page')
            return redirect('account:login')
    
    if request.method == 'POST':
        return render(request, 'ride/driver.html')


def sharer(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'ride/sharer.html')
        else:
            messages.error(request, 'You must be logged in to share a ride')
            return redirect('account:login')

def ride_status(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            ride = Ride.objects.filter(owner=request.user)[0]
            return render(request, 'ride/ride_status.html', {'ride': ride})
        else:
            messages.error(request, 'You must be logged in to view your ride status')
            return redirect('account:login')
    if request.method == 'POST':
        return render(request, 'ride/ride_status.html')
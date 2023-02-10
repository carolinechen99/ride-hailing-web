from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Import models
from .models import Ride
from account.models import Account
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
        vehicle_type = request.POST.get('car-type')
        special = request.POST.get('special')

        # owner = get_object_or_404(User, pk=request.user.id)
        try:
            owner = User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            messages.error(request, 'You are not logged in')
            return redirect('account:login')
        r = Ride(owner=owner, owner_party_size=party_size, required_arrival_time=arr_time, pickup_location=pickup_location,
                 destination=destination, allow_sharing=allow_sharing, vehicle_type=vehicle_type, special_requirements=special)
        r.save()
        messages.success(request, 'Your ride request has been submitted')
        return HttpResponseRedirect(reverse('ride:ride_status', args=(r.rid,)))
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

    return render(request, 'ride/driver.html')


def sharer_request(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'ride/sharer_request.html')
        else:
            messages.error(request, 'You must be logged in to share a ride')
            return redirect('account:login')
    if request.method == 'POST':
        destination = request.POST.get('destination')
        start_window = request.POST.get('start-window')
        end_window = request.POST.get('end-window')
        party_size = int(request.POST.get('party-size'))

        # get a list of all rides that has the same destination
        # and the required arrival time is within the start and end window
        # and the ride is open
        # and the ride is not the user's own ride
        # and the ride is sharing allowed
        query_list = Ride.objects.filter(destination=destination).filter(required_arrival_time__gte=start_window).filter(
            required_arrival_time__lte=end_window).filter(status='OP').exclude(owner=request.user).filter(allow_sharing=True)

        # check owner party size and subtract vehicle capacity to get available space
        for ride in query_list:

            available_space = calc_available_space(ride)

            # if the available space is less than the party size, remove the ride from the list
            if available_space < party_size:
                query_list = query_list.exclude(rid=ride.rid)

        # if there is no ride that matches the criteria, return an error message
        if not query_list:
            messages.error(request, 'No ride is available')
            return redirect('ride:sharer_request')

        context = {
            'rides': query_list,
            'party': str(party_size)  # keep the party size to use later
        }

        return render(request, 'ride/sharer_select.html', context)


def calc_available_space(ride):
    # if the ride already have sharers, add up the party size of all sharers
    current_sharer_size = 0
    if ride.sharers_username:
        for party in ride.sharers_party_size:
            current_sharer_size += party
    # calculate the number of current riders
    curr_riders = ride.owner_party_size + current_sharer_size

    # set the overall limit of the ride
    if ride.vehicle_type:
        limit = 7 if ride.vehicle_type == 'MV' else 4
    else:
        limit = 4

    # calculate the available space
    return limit - curr_riders


def sharer_select(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.error(
                request, 'You must be sending a share request to access this page')
            return render(request, 'ride/sharer_request.html')
        else:
            messages.error(request, 'You must be logged in to share a ride')
            return redirect('account:login')
    if request.method == 'POST':
        rid = request.POST.get('rid')
        party_size = request.POST.get('party-size')
        ride = Ride.objects.get(rid=rid)
        if not ride.sharers_username:
            ride.sharers_username = []
            ride.sharers_party_size = []
        ride.sharers_username.append(request.user.username)
        ride.sharers_party_size.append(int(party_size))
        ride.save()
        return HttpResponseRedirect(reverse('ride:ride_status', args=(int(rid),)))


def ride_status(request, ride_rid):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # Get all open/confirmed rides that belong to the user
            all_rides = Ride.objects.filter(owner=request.user).exclude(
                status='CP').exclude(status='CL')
            # Get all rides that the user is a sharer

            sharer_rides = Ride.objects.filter(sharers_username__contains=[
                                               request.user.username]).exclude(status='CP').exclude(status='CL')

            all_rides = all_rides | sharer_rides
            # Get the ride that the user is looking for
            ride = Ride.objects.get(rid=ride_rid)
            if ride.status == 'CF':
                driver = Account.objects.get(username=ride.driver.username)
                return render(request, 'ride/ride_status.html', {'ride': ride, 'driver': driver, 'all_rides': all_rides})
            return render(request, 'ride/ride_status.html', {'ride': ride, 'driver': None, 'all_rides': all_rides})
        else:
            messages.error(
                request, 'You must be logged in to view your ride status')
            return redirect('account:login')
    if request.method == 'POST':
        destination = request.POST.get('destination')
        pickup_location = request.POST.get('pickup-loc')
        arr_time = request.POST.get('arr-time')
        party_size = request.POST.get('party-size')
        allow_sharing = request.POST.get('allow-sharing') == 'allow'
        vehicle_type = request.POST.get('vehicle-type')
        special = request.POST.get('special')

        # Get the ride that the user is changing
        ride = Ride.objects.get(rid=ride_rid)
        # if the ride is already confirmed, return an error message
        if ride.status == 'CF':
            messages.error(
                request, 'Sorry, your driver is on the way. You cannot modify anymore')
            return redirect('ride:ride_status', ride_rid=ride_rid)
        # if the ride is already completed, return an error message
        if ride.status == 'CP':
            messages.error(request, 'Sorry, your ride is already completed')
            return redirect('ride:ride_status', ride_rid=ride_rid)
        # if the ride is already cancelled, return an error message
        if ride.status == 'CL':
            messages.error(request, 'Sorry, your ride is already cancelled')
            return redirect('ride:ride_status', ride_rid=ride_rid)
        # if the destination or arrival time or allow sharing or vehicle type is changed, create a new ride
        if destination != ride.destination or arr_time != ride.arr_time or allow_sharing != ride.allow_sharing or vehicle_type != ride.vehicle_type:
            # set up a new ride
            new_ride = Ride(
                owner=request.user,
                destination=destination,
                pickup_location=pickup_location,
                arr_time=arr_time,
                owner_party_size=party_size,
                allow_sharing=allow_sharing,
                vehicle_type=vehicle_type,
                special=special
            )
            new_ride.save()
            # update the old ride to cancelled
            ride.status = 'CL'
            ride.save()
            return redirect('ride:ride_status', ride_rid=new_ride.rid)

        # if the party size is changed, and is still less than what the vehicle can hold, update the ride
        if party_size != ride.owner_party_size:
            available = calc_available_space(ride)
            if party_size - ride.owner_party_size <= available:
                ride.owner_party_size = party_size
                ride.save()
                # display a message saying change is successful
                messages.success("Your ride has been updated successfully")
                return redirect('ride:ride_status', ride_rid=ride_rid)
            else:
                # set up a new ride
                new_ride = Ride(
                    owner=request.user,
                    destination=destination,
                    pickup_location=pickup_location,
                    arr_time=arr_time,
                    owner_party_size=party_size,
                    allow_sharing=allow_sharing,
                    vehicle_type=vehicle_type,
                    special=special
                )
                new_ride.save()
                # update the old ride to cancelled
                ride.status = 'CL'
                ride.save()
                return redirect('ride:ride_status', ride_rid=new_ride.rid)

        # if the pickup location or special is changed, update the ride
        if pickup_location != ride.pickup_location or special != ride.special:
            ride.pickup_location = pickup_location
            ride.special = special
            ride.save()
            # display a message saying change is successful
            messages.success("Your ride has been updated successfully")
            return redirect('ride:ride_status', ride_rid=ride_rid)


def driver_find_ride(request):
    # Get the driver(loggined user)'s vehicle type
    driver_vehicle_type = Account.objects.get(
        username=request.user.username).vehicle_type
    driver_vehicle_seats = Account.objects.get(
        username=request.user.username).vehicle_seats
    # Get all open rides
    # vehicle_seats should be greater than or equal to the party size of the ride
    # driver_vehicle_type should be the same as the vehicle type of the ride or the vehicle type of the ride is null
    # driver cannot be the owner of the ride
    query_list = Ride.objects.filter(status='OP', owner_party_size__lte=driver_vehicle_seats).filter(
        Q(vehicle_type__iexact=driver_vehicle_type) | Q(vehicle_type__isnull=True)).filter(~Q(owner=request.user))

    # Filter by pickup location
    ############################ DEBUGGING:pickup-loc/pickup_location################################
    if 'pickup-loc' in request.GET:
        pickup = request.GET['pickup-loc']
        if pickup:
            query_list = query_list.filter(pickup_location__iexact=pickup)

    # Filter by destination
    if 'destination' in request.GET:
        destination = request.GET['destination']
        if destination:
            query_list = query_list.filter(destination__iexact=destination)

    # Filter by arrival time
    if 'arr-time' in request.GET:
        arr_time = request.GET['arr-time']
        if arr_time:
            # if driver's arrival time is earlier than customer's arrival time, then the ride is not available
            query_list = query_list.filter(required_arrival_time__gte=arr_time)

    context = {
        'rides': query_list,
        'values': request.GET  # keep the search values when search is done
    }

    return render(request, 'ride/driver_find_ride.html', context)


def driver_ride_status(request, ride_rid):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # retrieve the ride using ride_rid get
            ride = Ride.objects.get(rid=ride_rid)
            # add the user to the driver of the ride
            ride.driver = request.user
            # change ride status to confirmed
            ride.status = 'CF'
            ride.save()

            # get rider's account
            rider_fn = ride.owner.username
            # get sharers' accounts
            sharer_accounts = []
            if ride.allow_sharing:
                if ride.sharers_username:
                    # get sharers' accounts by username, sharer's username is the first element of the sharer tuple
                    # example json data of sharers with only one sharer with username 'sharer1': [{"sharer1": 1}]
                    for usrn in ride.sharers_username:
                        sharer_accounts.append(
                            Account.objects.get(username=usrn))

            # create new array to store shares' username, first name and party size
            sharers = []
            for (sharer, party) in zip(sharer_accounts, ride.sharers_party_size):
                new = {'username': sharer.username,
                       'firstname': sharer.first_name,
                       'party': party}

                sharers.append(new)

            context = {
                'ride': ride,
                'rider': rider_fn,
                'sharers': sharers
            }

            return render(request, 'ride/driver_ride_status.html', context)
        else:
            messages.error(
                request, 'You must be logged in to view your ride status')
            return redirect('account:login')

    if request.method == 'POST':
        # retrieve the ride using ride_rid get
        ride = Ride.objects.get(rid=ride_rid)
        # change ride status to completed
        ride.status = 'CP'
        ride.save()
        messages.success(request, 'Your ride has been completed')

        # redirect to driver page
        return redirect('ride:driver')

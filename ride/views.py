from django.shortcuts import render
from django.http import HttpResponse
from ride.models import Ride, User

def request_ride(request):
    if request.method == 'POST':
        # Get form values
        destination = request.POST['destination']
        arr_time = request.POST['arr_time']
        party_size = request.POST['party-size']
        allow_sharing = request.POST['allow-sharing']
        car_type = request.POST['car-type']
        special = request.POST['special']
    r = Ride(owner_id='Beatles Blog', owner_party_size = party_size, required_arrival_time = arr_time, destination = destination, allow_sharing = allow_sharing, car_type = car_type, special = special)
    b.save()
    return render(request, 'ride/request_ride.html')
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
# Import models
from .models import Ride, Account


def request_ride(request):
    if request.method == 'POST':
        # Get form values
        destination = request.POST['destination']
        pickup_location = request.POST['pickup-location']
        arr_time = request.POST['arr-time']
        party_size = request.POST['party-size']
        allow_sharing = request.POST['allow-sharing']
        car_type = request.POST['car-type']
        special = request.POST['special']
    owner = get_object_or_404(Account, pk=request.user.id)
    r = Ride(owner_id='Beatles Blog', owner_party_size = party_size, required_arrival_time = arr_time, pickup_location = pickup_location, destination = destination, allow_sharing = allow_sharing, car_type = car_type, special = special)
    r.save()
    return render(request, 'ride/request_ride.html')
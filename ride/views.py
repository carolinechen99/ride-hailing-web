from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
# Import models
from .models import Ride
from account.models import Account
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/account/login')
def request_ride(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        print(destination)
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
            return redirect('account:login')
        r = Ride(owner = owner, owner_party_size = party_size, required_arrival_time = arr_time, pickup_location = pickup_location, destination = destination, allow_sharing = allow_sharing,  special_requirements = special)
        r.save()
        # messages.success(request, 'Successfully registered, now ready to login')
    return render(request, 'ride/request_ride.html')
    
from django.shortcuts import render
from django.http import HttpResponse

def request_ride(request):
    return render(request, 'ride/request_ride.html')
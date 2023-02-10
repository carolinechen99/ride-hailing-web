from django.urls import path

from . import views

app_name = 'ride'
urlpatterns = [
    path('request_ride', views.request_ride, name='request_ride'), 
    path('driver', views.driver, name='driver'),
    path('sharer_request', views.sharer_request, name='sharer_request'),
    path('sharer_select', views.sharer_select, name='sharer_select'),
    path('ride_status/<int:ride_rid>', views.ride_status, name='ride_status'),
    path('driver_find_ride', views.driver_find_ride, name='driver_find_ride'),
    # since Ride tables' primary key is 'rid', therefore driver_ride_status's url is 'driver_ride_status/<int:ride_rid>'
    path('driver_ride_status/<int:ride_rid>', views.driver_ride_status, name='driver_ride_status'),
]
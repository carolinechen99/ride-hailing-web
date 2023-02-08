from django.urls import path

from . import views

app_name = 'ride'
urlpatterns = [
    path('request_ride', views.request_ride, name='request_ride'), 
    path('driver', views.driver, name='driver'),
    path('sharer', views.sharer, name='sharer'),
    path('ride_status', views.ride_status, name='ride_status'),
    path('driver_find_ride', views.driver_find_ride, name='driver_find_ride'),
    path('driver_ride_status', views.driver_ride_status, name='driver_ride_status'),
]
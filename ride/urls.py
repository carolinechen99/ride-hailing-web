from django.urls import path

from . import views

app_name = 'ride'
urlpatterns = [
    path('request_ride', views.request_ride, name='request_ride'), 
]
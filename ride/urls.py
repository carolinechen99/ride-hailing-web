from django.urls import path

from . import views

urlpatterns = [
    path('request_ride', views.request_ride, name='request_ride'), 
]
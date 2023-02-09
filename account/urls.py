from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.login, name='login'), 
    path('register', views.register, name = 'register'), 
    path('logout', views.logout, name = 'logout'), 
    path('profile', views.profile, name = 'profile'),
    path('driver_register', views.driver_register, name = 'driver_register'),
    path('delete_driver_account', views.delete_driver_account, name = 'delete_driver_account')
]
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser', views.CreateUser.as_view(), name='CreateUser'),
    path('index', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('createvehicales', views.CreateVehicales.as_view(), name=' CreateVehicales'),
    path('bookingcar', views.Booking.as_view(), name='Booking'),
]
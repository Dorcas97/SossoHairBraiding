from rest_framework import viewsets
from rest_framework import generics
from .models import Stylist, Client, Hairstyle, Appointment
from .serializers import (
    StylistSerializer, ClientSerializer, HairstyleSerializer, AppointmentSerializer, RegisterSerializer
)


class StylistViewSet(viewsets.ModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class HairstyleViewSet(viewsets.ModelViewSet):
    queryset = Hairstyle.objects.all()
    serializer_class = HairstyleSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

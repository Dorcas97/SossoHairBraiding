from django.contrib import admin
from .models import Stylist, Client, Hairstyle, Appointment


@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'address']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Hairstyle)
class HairstyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['stylist', 'client', 'date', 'appointment_time']
    list_filter = ['stylist', 'client', 'date']
    search_fields = ['stylist__name', 'client__name', 'date']

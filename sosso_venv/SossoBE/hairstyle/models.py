from django.db import models
import datetime
from django.contrib.auth.models import User


class Stylist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Hairstyle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=300, blank=True, null=True)
    image = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    hairstyle = models.ForeignKey(Hairstyle, on_delete=models.CASCADE)
    date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with {self.stylist.name} on {self.date} at {self.appointment_time}"

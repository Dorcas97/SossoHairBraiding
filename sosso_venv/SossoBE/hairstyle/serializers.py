from rest_framework import serializers
from .models import Stylist, Client, Hairstyle, Appointment
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class StylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stylist
        fields = ['id', 'user', 'name', 'phone', 'email', 'address']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'name', 'phone', 'email']


class HairstyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hairstyle
        fields = ['id', 'name', 'description', 'image', 'price']


class AppointmentSerializer(serializers.ModelSerializer):
    stylist = StylistSerializer()
    client = ClientSerializer()
    hairstyle = HairstyleSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'stylist', 'client', 'hairstyle', 'date', 'appointment_time', 'created_at', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

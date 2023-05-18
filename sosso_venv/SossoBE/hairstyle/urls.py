from django.urls import path, include
from rest_framework import routers
from .views import StylistViewSet, ClientViewSet, HairstyleViewSet, AppointmentViewSet, RegisterView

router = routers.DefaultRouter()
router.register('stylists', StylistViewSet)
router.register('clients', ClientViewSet)
router.register('hairstyles', HairstyleViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),

]
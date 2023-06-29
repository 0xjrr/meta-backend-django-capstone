from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'menu', MenuItemsView, basename='menu')
router.register(r'booking', BookingView, basename='booking')

urlpatterns = [
    path('', index, name='home'),
    path('', include(router.urls)),
]
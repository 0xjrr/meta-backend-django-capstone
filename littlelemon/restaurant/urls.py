from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'menu', MenuItemsView, basename='menu')
router.register(r'booking', BookingView, basename='booking')

urlpatterns = [
    path('', index, name='home'),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]